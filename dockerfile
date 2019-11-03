FROM ubuntu:18.04

MAINTAINER Sobia Khalid "sobia.khalid.2126@gmail.com"

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get install -y python3-mysqldb

ENV LANG C.UTF-8  
ENV LANGUAGE C:en  
ENV LC_ALL C.UTF-8

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt 

COPY . /

ENV FLASK_APP run.py

RUN nose2 -v

CMD [ "flask", "run", "--host", "0.0.0.0" ]
 