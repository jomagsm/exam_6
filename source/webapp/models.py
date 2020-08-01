from django.db import models

DEFAUL_STATUS = 'active'
STATUS_CHOICE = [(DEFAUL_STATUS, 'Активно'), ('blocked', 'Заблокированно')]


class Note(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='Время изменения')
    status = models.CharField(max_length=20, verbose_name='Статус', choices=STATUS_CHOICE, default=DEFAUL_STATUS)


