# Email reader bot
Получает новые письма, полученные на ящики электронной почты, в чат-боте для Telegram с возможностью отслеживания нескольких ящиков и фильтрации писем по их отправителям.

## Основные технологии разработки продукта

- Docker
- Django 4.1 (async)
- PostgreSQL 15
- Celery
- aiogram


## Развертывание проекта

Для запуска проекта используйте Docker compose:
`docker compose -f docker-compose.yml --env-file .env.dev up -d --build`

- Минимальные переменные окружения для запуска проекта
```shell
ENV_FILENAME=<ваш файл переменных окружения>
DEBUG=False
ALLOWED_HOSTS=0.0.0.0,127.0.0.1,172.17.0.1,mail_sender_app

EMAIL_SENDER_DIR=email_sender
BOT_DIR=email_sender/telegram_bot

POSTGRES_DATABASE=mail_sender_app
POSTGRES_USER=mail_sender_app
POSTGRES_PASSWORD=mail_sender_app
POSTGRES_HOST=mail_sender_postgres_db
POSTGRES_PORT=5432

DJANGO_ALLOW_ASYNC_UNSAFE=true
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@mail.ru
SECRET_KEY=<ваш секретный код>
SENTRY_DSN=<ваш dsn>

ENCRYPTION_ALGORITHM=RSA
ENCRYPTION_ENCODING=utf-8
PUBLIC_KEY=<ssh private key>
PRIVATE_KEY=<ssh public key>

API_TOKEN=<bot token>

USERS_URL=http://172.17.0.1:8000/api/v1/users/
LINK_MAIL_URL=http://172.17.0.1:8000/api/v1/users/mail/{0}/
LINK_SENDER_URL=http://172.17.0.1:8000/api/v1/users/mail_sender/{0}/
LIST_MAILS_URL=http://172.17.0.1:8000/api/v1/users/mails/
LIST_SENDERS_URL=http://172.17.0.1:8000/api/v1/users/senders/
LIST_PROVIDERS_URL=http://172.17.0.1:8000/api/v1/providers/

CELERY_BROKER_URL=redis://mail_sender_redis
CELERY_RESULT_BACKEND=redis://mail_sender_redis

FLOWER_USER=flower
FLOWER_PASSWORD=flower
```

Все доступные переменные окружения представлены в файле .env.template

- Внешние порты:
* 8000 - API бэкенда
* 5432 - база данных

## Разработчики проекта

- Даниил Ярошенко @d.yaroshenko [d.yaroshenko@ylab.io]
- Янкина Олеся @o.yankina [o.yankina@ylab.io]
- Кучкаров Азамат @a.kuchkarov [a.kuchkarov@ylab.io]
- Семенюк Максим @m.semenyuk [m.semenyuk@ylab.io]

## Схема взаимодействия с внешними сервисами

Пример схемы взаимодействия сервисов:

[Sequnce Diagrams](https://app.diagrams.net/#G1vrZ2M973VHvNOOebRDPdYykK0LnnZhc4)

## Схема БД проекта и применение миграций

Пример схемы бд:

[ERD](https://app.diagrams.net/#G1Yvqkbhp8G8SE_K_ym98PLiOlVVaau7_n)

## Структура веток проекта
- master - актуальная production ветка проекта
- develop - ветка основной разработки

## Тестирование
Для запуска тестов:
`docker compose -f docker-compose-test.yml --env-file .env.dev up -d --build`
