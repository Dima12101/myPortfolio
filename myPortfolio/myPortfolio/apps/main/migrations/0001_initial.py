# Generated by Django 2.2.1 on 2019-09-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='имя автора')),
                ('comment_text', models.CharField(max_length=200, verbose_name='текст комментария')),
                ('date', models.DateTimeField(verbose_name='дата комментария')),
            ],
        ),
    ]
