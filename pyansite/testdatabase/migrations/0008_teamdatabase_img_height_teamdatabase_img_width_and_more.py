# Generated by Django 5.0.1 on 2024-02-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdatabase', '0007_alter_teamdatabase_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamdatabase',
            name='img_height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='teamdatabase',
            name='img_width',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teamdatabase',
            name='img',
            field=models.ImageField(height_field='img_height', upload_to='images/', width_field='img_width'),
        ),
    ]
