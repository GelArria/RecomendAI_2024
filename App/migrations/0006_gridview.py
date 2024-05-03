# Generated by Django 5.0.4 on 2024-05-03 15:23

import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_rename_unknownmovies_knownmovie_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='gridView',
            fields=[
                ('idUser', models.AutoField(primary_key=True, serialize=False)),
                ('genreGrid', jsonfield.fields.JSONField()),
                ('binaryY', models.BinaryField()),
                ('binarySeen', models.BinaryField()),
            ],
        ),
    ]