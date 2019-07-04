#!/usr/bin/env bash

rm -f db.sqlite3
./manage.py migrate
./manage.py populate
./manage.py createinitialrevisions
./manage.py runserver
