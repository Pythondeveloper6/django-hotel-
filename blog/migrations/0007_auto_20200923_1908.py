# Generated by Django 3.1.1 on 2020-09-23 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200923_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]