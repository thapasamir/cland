# Generated by Django 3.1.4 on 2021-01-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210127_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cateogies',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='content',
            name='acess',
        ),
        migrations.AddField(
            model_name='content',
            name='acess',
            field=models.ManyToManyField(to='main.cateogies'),
        ),
    ]
