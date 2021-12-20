FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV UVICORN_CMD_ARGS ""

EXPOSE 8000
WORKDIR /app

COPY poetry.lock pyproject.toml ./

ARG CI_JOB_TOKEN=""
ARG GIT_HOST=""
ARG GIT_PASSWORD=${CI_JOB_TOKEN}
ARG GIT_LOGIN="gitlab-ci-token"

RUN echo -e "machine ${GIT_HOST}\nlogin ${GIT_LOGIN}\npassword ${GIT_PASSWORD}" > ~/.netrc && \
    apt-get update && \
    apt-get install -y git && \
    pip install poetry==1.1.0 --no-cache-dir && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    rm -rf /root/.cache/pypoetry && \
    rm -rf ~/.netrc && \
    apt-get clean autoclean && \
    apt-get autoremove --yes && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY . .
ARG CI_COMMIT_SHA=""
ENV GIT_COMMIT_SHA=${CI_COMMIT_SHA}

CMD update-ca-certificates && \
    alembic upgrade head && \
    uvicorn --host=0.0.0.0 $UVICORN_CMD_ARGS app.main:app
