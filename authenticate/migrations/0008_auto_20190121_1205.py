# Generated by Django 2.1.4 on 2019-01-21 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0007_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
