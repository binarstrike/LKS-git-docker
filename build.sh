#!/bin/sh
TAG=flask-webserver
if [ ! -z "$@" ]; then
    docker build "$@" --tag $TAG .
else
    docker build --tag $TAG .
fi
