FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV UVICORN_CMD_ARGS ""

EXPOSE 8000
WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry==1.1.12 --no-cache-dir && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev && \
    rm -rf /root/.cache/pypoetry

COPY alembic.ini ./
COPY smartapp_files smartapp_files
COPY app app

ARG CI_COMMIT_SHA=""
ENV GIT_COMMIT_SHA=${CI_COMMIT_SHA}

CMD update-ca-certificates && \
    alembic upgrade head && \
    uvicorn --host=0.0.0.0 $UVICORN_CMD_ARGS app.main:app