FROM python:3.13-alpine

MAINTAINER Kirill Khokhlov

ENV PYTHONUNBUFFERED=1
# for postgres libpq-dev
RUN apk update
RUN apk add --no-cache gcc musl-dev mariadb-dev
# for pillow
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /tmp

RUN cd /tmp && pip install -r requirements.txt