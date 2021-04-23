FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

RUN pip install --upgrade tgcf

RUN tgcf --version && tg-login --version

CMD ["tgcf"]
