from django.db import models


class User(models.Model):

    name = models.CharField('Ник', max_length=100)
    password = models.TextField('Пароль', max_length=500)
    email = models.EmailField('E-mail')

    def __str__(self):
        return self.name
