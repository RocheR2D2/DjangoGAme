# Generated by Django 2.1.4 on 2019-01-21 18:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0010_auto_20190121_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followedby', to=settings.AUTH_USER_MODEL),
        ),
    ]