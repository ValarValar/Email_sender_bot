# Generated by Django 4.1.7 on 2023-03-20 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MailProvider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="Название"
                    ),
                ),
                ("server", models.TextField(verbose_name="Адрес сервера")),
                ("port", models.IntegerField(verbose_name="Порт")),
            ],
            options={
                "verbose_name": "Провайдер",
                "verbose_name_plural": "Провайдеры",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tg_id",
                    models.BigIntegerField(
                        unique=True, verbose_name="Идентификатор в телеграм"
                    ),
                ),
                ("first_name", models.CharField(max_length=150, verbose_name="Имя")),
                (
                    "second_name",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Фамилия"
                    ),
                ),
                (
                    "registered_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата регистрации"
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.CreateModel(
            name="TrackedMailSender",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=256, verbose_name="Электронный адрес"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.user"
                    ),
                ),
            ],
            options={
                "verbose_name": "Отправитель",
                "verbose_name_plural": "Отправители",
            },
        ),
        migrations.CreateModel(
            name="Mail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=256, unique=True, verbose_name="Электронный адрес"
                    ),
                ),
                ("password", models.TextField(verbose_name="Пароль для приложений")),
                (
                    "provider",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.mailprovider",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.user"
                    ),
                ),
            ],
            options={
                "verbose_name": "Почта",
                "verbose_name_plural": "Почты",
            },
        ),
    ]
