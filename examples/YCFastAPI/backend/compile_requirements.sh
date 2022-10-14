#!/usr/bin/env bash

poetry export --without-hashes -f requirements.txt --output requirements.txt
