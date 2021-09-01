#!/usr/bin/env bash

git clone https://github.com/teadove/fastapi-boilerplate
cd fastapi-boilerplate
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install poetry
poetry install

cookiecutter ./