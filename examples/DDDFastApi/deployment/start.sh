#!/usr/bin/env bash

source .venv/bin/activate
cd ../services/main
exec python entrypoints.py
