from django.contrib.auth.models import AbstractUser
from django.db import models

from mailing.models import NULLABLE


class User(AbstractUser):
    """Модель пользователя"""
    username = None  # поле username удалится
    # заменим способ авторизации через email, который нужно переопределить:
    email = models.EmailField(unique=True, verbose_name='почта')  # поле уникальное

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)

    is_active = models.BooleanField(default=False, verbose_name='статус активности')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('is_active',)

