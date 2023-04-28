#!/usr/bin/env bash

echo "Starting Backend..."

pipenv run ./manage.py makemigrations
pipenv run ./manage.py migrate
pipenv run ./manage.py runserver 0.0.0.0:8000
