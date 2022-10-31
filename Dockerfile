FROM python:3.10-slim-buster

RUN apt update && apt install --yes git gcc libcurl4-openssl-dev libssl-dev

ENV \
    PYTHONPATH=api \
    DJANGO_SETTINGS_MODULE=api.settings.dev

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /app
CMD poetry run gunicorn --workers=2 --threads=2 --bind 0.0.0.0:8000 api.wsgi
