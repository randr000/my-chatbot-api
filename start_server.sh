#!/bin/sh
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app