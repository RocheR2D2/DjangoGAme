# Generated by Django 2.1.4 on 2019-01-21 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hs_game', '0010_auto_20190121_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='cards', to='authenticate.UserProfile'),
        ),
    ]