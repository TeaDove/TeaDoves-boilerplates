#!/usr/bin/env bash

git clone https://github.com/teadove/fastapi-boilerplate
cd fastapi-boilerplate || exit
pip3 install cookiecutter

cookiecutter ./