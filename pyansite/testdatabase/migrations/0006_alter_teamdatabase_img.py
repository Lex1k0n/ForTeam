# Generated by Django 5.0.1 on 2024-02-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdatabase', '0005_alter_teamdatabase_href'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamdatabase',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
