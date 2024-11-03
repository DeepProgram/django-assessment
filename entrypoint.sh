#!/bin/bash

while ! nc -z db 3306; do
  echo "Waiting for the database to be ready..."
  sleep 1
done

echo "Database is ready! Starting Django server..."

python core/manage.py makemigrations
python core/manage.py migrate
python core/manage.py runserver 0.0.0.0:5000