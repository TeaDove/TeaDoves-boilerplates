#!/bin/bash
# Скрипт для перезалива

git pull

supervisorctl restart fastapi-server