#!/bin/sh
gunicorn --timeout 1000 --workers 1 --bind 0.0.0.0:5000 app:app