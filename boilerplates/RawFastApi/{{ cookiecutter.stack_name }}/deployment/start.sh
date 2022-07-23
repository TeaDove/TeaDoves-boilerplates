#!/usr/bin/env bash

source .venv/bin/activate
cd ../services/main
exec uvicorn entrypoints:uvicorn_app
