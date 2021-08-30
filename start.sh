#!/bin/bash
# Скрипт для запуска сервера, если существует .venv, активирует его

[ -d ".venv" ] && source .venv/bin/activate

exec python3 -m app
