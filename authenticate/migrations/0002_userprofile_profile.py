# Generated by Django 2.1.4 on 2019-01-20 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/userprofiles'),
        ),
    ]