#!/bin/bash
set -o errexit

# Add this before installing requirements
pip install --upgrade pip setuptools wheel
pip install cython==3.0.0

# Install requirements
pip install -r requirements.txt

# Rebuild scikit-learn
pip install --no-build-isolation --force-reinstall scikit-learn

# Standard Django commands
python manage.py collectstatic --noinput
python manage.py migrate
