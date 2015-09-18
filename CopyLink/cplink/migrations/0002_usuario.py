# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cplink', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=254)),
                ('first_name', models.CharField(max_length=30, blank=True)),
                ('last_name', models.CharField(max_length=30, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('synergy_level', models.IntegerField()),
                ('is_team_player', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
