## FastAPI boilerplate
Quickstart для бекенд сервера на FastAPI. Включает в себя конфиги для nginx, systemd,
supervisord и docker.

## Установка
- Склонируйте репозиторий и установите coockiecutter:<br>
``` bash
git clone https://github.com/teadove/fastapi-boilerplate
cd fastapi-boilerplate 
pip3 install cookiecutter
```
- Запустите кукикаттер:
``` bash
cookiecutter ./
```
- Заполнить данные:
``` yaml
project_name: Название проекта
project_slug: Ярлык проекта(используется в конфигах и папках, не используйте пробелы и 
              заглавные буквы)
description: Описание проекта
hostname: Название хоста
env_filename: Название файла конфигурации(лучше оставить умолчательное)
```
- Скопируйте созданную папку с проектом в нужный репозиторий 
- Радуйтесь!

## Cookiecutter
Coockiecutter - библиотека на python, позволяющая создавать шаблоны и по ним генерировать файлы.<br>
После использования вышеуказанного скрипта вам будет предложено выбрать 
называние проекту и его хостнейм.  
Если вы не хотите использовать шаблонизацию, то можете просто 
склонировать репозиторий, изменить название папки `{{ сoockiecutter.project_name }}` и 
конфигурацию в `conf.d`.

## Зависимости
```python
python = "^3.8"
fastapi = "^0.68.1"
pydantic = {extras = ["dotenv"], version = "^1.8.2"}
uvicorn = "^0.15.0"
cookiecutter = "^1.7.3"
loguru = "^0.5.3"
```

## Утилы
- `start.sh` - включение .venv и сервера
- `setup.sh` - установка зависимостей

## Contribute
Если вы хотите помочь проекту, залейте пул реквест.  
Для обратной связи пишите в тг: [@teadove](https://t.me/teadove)

## TODO 
- [X] контейнерезировать
- [X] конфиг systemd
- [X] coockiecutter
- [ ] автоустановщик **всех нужных** пакетов для дебиана