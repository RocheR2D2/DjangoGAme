# Generated by Django 2.1.4 on 2019-01-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_auto_20190120_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/userprofiles'),
        ),
    ]