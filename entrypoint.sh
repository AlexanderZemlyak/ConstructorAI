#!/bin/bash

export FLASK_APP=app.py

exec gunicorn -b 0.0.0.0:5005 --workers 4 app:app