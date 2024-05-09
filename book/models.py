from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')

    description = models.TextField(blank=True, verbose_name='Описание')

    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.title