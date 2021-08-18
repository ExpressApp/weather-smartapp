import uuid
import warnings
from typing import Any, Callable

import docker
import docker.errors
import pytest
from docker import APIClient

from tests.utils import do_with_retry


@pytest.fixture(scope="session")
def docker_client() -> docker.APIClient:
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    with docker.APIClient(version="auto") as client:
        yield client


@do_with_retry(docker.errors.APIError, RuntimeError, "cannot pull postgres image")
def pull_image(client: APIClient, image: str, printer) -> None:  # pragma: no cover
    printer(f"pulling image: {image}")
    client.pull(image)


def create_container(
    docker_client: APIClient, image: str, printer: Callable
) -> Any:  # pragma: no cover
    pull_image(docker_client, image, printer=printer)
    name = "test-postgres-{}".format(uuid.uuid4())
    ports = [5432]

    printer(f"creating container: {name}, {ports}, {image}")

    container = docker_client.create_container(
        image=image,
        name=name,
        ports=ports,
        detach=True,
    )
    return container
