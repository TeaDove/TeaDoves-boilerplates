## {{ cookiecutter.project_name }}

## Утилиты
`./setup.sh` - создание .venv и установка зависимостей
`./start.sh` - запуск сервера

## Зависимости
```python
python = "^3.8"
fastapi = "^0.68.1"
pydantic = {extras = ["dotenv"], version = "^1.8.2"}
uvicorn = "^0.15.0"
cookiecutter = "^1.7.3"
loguru = "^0.5.3"
```