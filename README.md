## FastAPI boilerplate
Quickstart для бекенд сервера на FastAPI. Включает в себя конфиги для nginx, 

## Автоматическая установка
`curl https://raw.githubusercontent.com/TeaDove/fastapi-boilerplate/master/auto_install.sh | sh`

## Зависимости
```python
python = "^3.7"
fastapi = "^0.68.1"
pydantic = {extras = ["dotenv"], version = "^1.8.2"}
uvicorn = "^0.15.0"
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
- [ ] coockiecutter
- [ ] автоустановщик **всех нужных** пакетов для дебиана