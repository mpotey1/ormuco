#!/bin/bash        
cd /home/django/django_project/
--workers 3 --bind 127.0.0.1:8000 django_project.wsgi:application
