#!/usr/bin/env bash

poetry export --without-hashes -f requirements.txt --output app/requirements.txt
