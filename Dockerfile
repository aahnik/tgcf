FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip && pip install poetry

COPY README.md LICENSE pyproject.toml poetry.lock ./

COPY src ./src

COPY tests ./tests

RUN poetry install

CMD ["poetry","run","tgcf"]
