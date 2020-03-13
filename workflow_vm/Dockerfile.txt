FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/nextstrain/ncov.git
RUN apt-get install -y npm
RUN npm install --global auspice

