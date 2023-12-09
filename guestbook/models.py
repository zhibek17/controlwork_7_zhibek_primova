from django.db import models

class StatusChoice(models.TextChoices):
    ACTIVE = 'active', 'Активно'
    BLOCKED = 'blocked', 'Заблокировано'

class GuestBook(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя')
    email = models.EmailField(null=False, blank=False, verbose_name='Почта')
    text = models.TextField(null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name='Время редактирования')
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.ACTIVE,
                              verbose_name='Статус')

    def __str__(self):
        return self.name
