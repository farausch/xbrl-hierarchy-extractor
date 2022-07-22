FROM python:3.8-slim-buster

RUN apt-get update && \
apt-get -y install gcc

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "api.py"]