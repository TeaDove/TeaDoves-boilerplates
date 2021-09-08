#!/usr/bin/env bash

python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install poetry
poetry install