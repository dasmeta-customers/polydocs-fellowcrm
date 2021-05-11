FROM python:3.6
ENV PYTHONUNBUFFERED 1
MAINTAINER Daniel Jordan <mail@danieljordan.de>
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip3 install --no-cache-dir -r requirements.txt