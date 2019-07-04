#!/usr/bin/env bash

python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py populate
./manage.py createinitialrevisions
./manage.py runserver
