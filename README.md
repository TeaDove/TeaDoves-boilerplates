## FastAPI boilerplate
Quickstart для бекенд сервера на FastAPI. Включает в себя конфиги для nginx, systemd,
supervisord и docker. Полное описание структуры, используемых библиотек, конфигураций и тд 
вы можете найти в [DESCRIPTION.md](https://vk.com)

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
- Скопируйте нужную вам конфигурацию. Подробнее читайте этот [ридми](https://vk.com).
- Радуйтесь!

## Cookiecutter
Coockiecutter - библиотека на python, позволяющая создавать шаблоны и по ним генерировать файлы.<br>
<br>
Если вы не хотите использовать шаблонизацию, то можете просто 
склонировать репозиторий, изменить название папки `{{ сoockiecutter.project_slug }}` и всю 
конфигурацию в `conf.d`.

## Утилиты
- `start.sh` - включение .venv и сервера
- `setup.sh` - установка зависимостей

## Contribute
Если вы хотите помочь проекту, не бойтесь отсылать пулл-реквесты или открывать issue.<br>
Для обратной связи пишите в тг: [@teadove](https://t.me/teadove)
