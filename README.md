## FastAPI boilerplate
Quickstart для бекенд сервера на FastAPI. Включает в себя конфиги для nginx, 

## Установка
- Запустить скрипт:<br>
`curl https://raw.githubusercontent.com/TeaDove/fastapi-boilerplate/master/auto_install.sh | bash`
- Скопировать созданную папку с проектом в нужный репозиторий 
- Радоваться

## Cookiecutter
После использования вышеуказанного скрипта вам будет предложено выбрать 
называние проекту и его хостнейм.  
Если вы не хотите использовать шаблонизацию, то можете просто 
склонировать репозиторий, изменить название папки `{{ сoockiecutter.project_name }}` и 
конфигурацию в `conf.d` и в `app/api/main.py`


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
- `auto_install.sh` - клонирование репозитория, установка зависимостей и включение сервера
- `redeploy.sh` - pull репозитория и перезагрузка сервера

## Contribute
Если вы хотите помочь проекту, залейте пул реквест.  
Для обратной связи пишите в тг: [@teadove](https://t.me/teadove)

## TODO 
- [ ] контейнерезировать
- [ ] конфиг systemd
- [X] coockiecutter
- [ ] автоустановщик **всех нужных** пакетов для дебиана