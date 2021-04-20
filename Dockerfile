FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip && pip install poetry

COPY . .

RUN poetry install

CMD ["poetry","run","tgcf"]
