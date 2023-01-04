### Установка
- Скачать [terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli) и [terragrunt](https://terragrunt.gruntwork.io/docs/getting-started/install/) (заходить из под ВПН)
### Команды
```shell
STAGE=stable terragrunt init -reconfigure # Инициализация, надо сделать 1 раз при смене стека

STAGE=stable terragrunt plan  # Планирование стека на стенд "stable"
STAGE=stable terragrunt apply # Выполнение стека на стенд "stable"
```
### Yandex Cloud
Чтобы что-то задеплоить, надо получить вынести YC_TOKEN в переменные окружения.<br>
Получить его можно тут: https://cloud.yandex.ru/docs/iam/concepts/authorization/oauth-token<br>
Норм пацаны вынесут его в [gopass](https://github.com/gopasspw/gopass) и будут делать так:
```shell
export YC_TOKEN=(yc iam create-token)
```

### Настройка
- Настройка стейджа и региона деплоймента ведется в `deploy_config.yaml`
- Настройка инфраструктуры ведется в файлах `*.tf`
