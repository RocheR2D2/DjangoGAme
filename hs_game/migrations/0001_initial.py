# Generated by Django 2.1.4 on 2019-01-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('mana', models.IntegerField(default=0)),
                ('attack', models.IntegerField(default=0)),
                ('health', models.IntegerField(default=0)),
                ('craftingcost', models.IntegerField(default=0)),
                ('arcane_dust_gained', models.IntegerField(default=0)),
                ('card_rarity', models.CharField(max_length=60, unique=True)),
                ('card_class', models.CharField(max_length=60, unique=True)),
                ('card_type', models.CharField(max_length=60, unique=True)),
                ('card_race', models.CharField(max_length=60, unique=True)),
                ('card_set', models.CharField(max_length=60, unique=True)),
                ('card_text', models.CharField(max_length=60, unique=True)),
                ('flavor_text', models.CharField(max_length=60, unique=True)),
                ('card_image', models.ImageField(null=True, unique=True, upload_to='images/cards')),
            ],
        ),
    ]
