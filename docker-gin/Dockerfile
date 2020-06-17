FROM golang:1.14
WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

ENV GO111MODULE  on
ENV GOPROXY  https://goproxy.io


COPY . /usr/src/app
CMD go run main.go

