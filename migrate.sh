#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate backend 0002