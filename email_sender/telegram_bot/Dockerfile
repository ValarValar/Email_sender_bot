## Базовый образ для сборки
FROM python:3.10-slim

# Указываем рабочую директорию
WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app/email_sender

# Запрещаем Python писать файлы .pyc на диск
ENV PYTHONDONTWRITEBYTECODE 1
# Запрещает Python буферизовать stdout и stderr
ENV PYTHONUNBUFFERED 1

# Установка зависимостей проекта
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

# Копируем проект
COPY . .
