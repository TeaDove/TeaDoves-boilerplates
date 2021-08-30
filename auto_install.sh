#!/usr/bin/env bash

git clone https://github.com/teadove/fastapi-boulerplate
cd fastapi-boulerplate
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install poetry
poetry install

touch .env # в .env положить настройки,
# список настроек в /app/core/settings.py
bash start.sh # Тестовый запуск