# FROM ubuntu:20.04
FROM python:3.9-alpine

RUN apk add --update alpine-sdk && \
    apk add linux-headers && \
    apk add --update --no-cache mariadb-connector-c-dev mariadb-dev && \
    apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev
#RUN apk add openrc busybox-initscripts
RUN apk add g++ gcc libxslt-dev
# RUN apt update
# RUN apt install -y g++ python3 cron python3 python3-pip python-dev default-libmysqlclient-dev libjpeg-dev zlib1g-dev
# RUN apt install -y cron

# SET CORRECT TIME
RUN apk add --no-cache tzdata
# ENV TZ Europe/Lisbon
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# RUN apt-get update
RUN mkdir /www
WORKDIR /www
# RUN pip install gunicorn
RUN pip3 install uwsgi

# INSTALL PYTHON REQUIREMENTS
COPY ./requirements.txt /www/
RUN pip3 install -r requirements.txt


# INSTALL APPLICATION
COPY . /www/


ENV PYTHONUNBUFFERED 1
