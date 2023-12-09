from django.db import models

status_choices = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class GuestBook(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя')
    email = models.EmailField(null=False, blank=False, verbose_name='Почта')
    text = models.TextField(null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    fixed_at = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name='Время редактирования')
    status = models.CharField(max_length=20, choices=status_choices, default=status_choices[0][0],
                              verbose_name='Статус')

    def __str__(self):
        return self.name