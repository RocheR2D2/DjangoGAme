# Generated by Django 2.1.4 on 2019-01-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0004_auto_20190120_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile',
            field=models.ImageField(blank=True, default='static/images/userprofiles/default.png', null=True, upload_to='static/images/userprofiles'),
        ),
    ]
