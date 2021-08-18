import warnings
from os import environ
from typing import Callable

import alembic.config
import docker
import psycopg2
import pytest

from tests.fixtures.docker import create_container
from tests.utils import do_with_retry

POSTGRES_DOCKER_IMAGE = "postgres:11.4-alpine"


@pytest.fixture(autouse=True)
def migrations(postgres_server):
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    alembic.config.main(argv=["upgrade", "head"])
    yield
    alembic.config.main(argv=["downgrade", "base"])


@pytest.fixture(scope="session", autouse=True)
def postgres_server(docker_client: docker.APIClient, printer: Callable) -> None:
    test_db_dsn = environ.get("TEST_DB_CONNECTION")
    use_local_db = environ.get("DB")

    if test_db_dsn:  # pragma: no cover
        environ["DB_CONNECTION"] = test_db_dsn
        printer("use custom db")
        ping_postgres(test_db_dsn, printer=printer)
        yield
    elif use_local_db:  # pragma: no cover
        default_dsn = environ["DEFAULT_TEST_DB_CONNECTION"]
        environ["DB_CONNECTION"] = default_dsn
        printer("use local db")
        ping_postgres(default_dsn, printer=printer)
        yield
    else:  # pragma: no cover
        printer("use container db")
        container = create_container(
            docker_client, POSTGRES_DOCKER_IMAGE, printer=printer
        )
        try:
            printer("run container")
            docker_client.start(container=container["Id"])
            inspection = docker_client.inspect_container(container["Id"])
            host = inspection["NetworkSettings"]["IPAddress"]
            docker_dsn = f"postgres://postgres:postgres@{host}/postgres"
            environ["DB_CONNECTION"] = docker_dsn
            ping_postgres(docker_dsn, printer=printer)
            yield
        finally:
            docker_client.kill(container["Id"])
            docker_client.remove_container(container["Id"])


@do_with_retry(psycopg2.OperationalError, RuntimeError, "cannot start postgres server")
def ping_postgres(dsn: str, *, printer):
    printer(f"pinging db with dsn: {dsn}")
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    cur.execute("SELECT now();")
    printer("db pong")
    cur.close()
    conn.close()
