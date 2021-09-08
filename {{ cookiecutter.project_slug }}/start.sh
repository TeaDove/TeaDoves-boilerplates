#!/usr/bin/env bash
# Скрипт для запуска сервера, если существует .venv, активирует его

[ -d "../.venv" ] && source ../.venv/bin/activate
[ -d ".venv" ] && source .venv/bin/activate
# export PATH=$PATH:/usr/local/go/bin

exec python3 -m app
