from django.db import models


class TeamDatabase(models.Model):

    img_width = 100
    img_height = 100
    nickname = models.CharField('Ник', max_length=50)
    desc = models.TextField('Описание', max_length=1000)
    img = models.ImageField(upload_to='images/', width_field='img_width', height_field='img_height')
    count = models.IntegerField('Число проектов')
    href = models.URLField('Ссылка', max_length=100, default='https://web.telegram.org/a/')

    def __str__(self):
        return self.nickname


class ProjectDatabase(models.Model):

    img_width = 200
    img_height = 150
    name = models.CharField('Название', max_length=50)
    desc = models.TextField('Описание', max_length=1000)
    img = models.ImageField(upload_to='images/', width_field='img_width', height_field='img_height')
    href = models.URLField('Ссылка', max_length=100, default='https://web.telegram.org/a/')

    def __str__(self):
        return self.name
