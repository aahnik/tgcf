FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip wheel setuptools poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT true

COPY . .

RUN poetry install

CMD poetry run tgcf
