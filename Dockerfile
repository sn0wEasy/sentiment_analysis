FROM python:3.9
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

ENV CONSUMER_KEY = ${CONSUMER_KEY}
ENV CONSUMER_SECRET = ${CONSUMER_SECRET}
ENV BEARER_TOKEN = ${BEARER_TOKEN}
ENV ACCESS_TOKEN = ${ACCESS_TOKEN}
ENV ACCESS_SECRET = ${ACCESS_SECRET}

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN python -m pip install jupyterlab
RUN python -m pip install requests_oauthlib
RUN python -m pip install tweepy

RUN apt install -y mecab libmecab-dev mecab-ipadic-utf8
RUN python -m pip install mecab-python3==0.7
RUN python -m pip install pymlask
RUN python -m pip install googletrans==4.0.0-rc1
RUN python -m pip install nltk