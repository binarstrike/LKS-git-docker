#!/bin/sh
TAG=flask-webserver:latest
if [ ! -z "$@" ]; then
    docker build "$@" --tag $TAG .
else
    docker build --tag $TAG .
fi
