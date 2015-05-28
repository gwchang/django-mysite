# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title_text', models.CharField(max_length=200)),
                ('author_text', models.CharField(max_length=200)),
                ('description_text', models.CharField(max_length=2000)),
                ('homepage_url', models.CharField(max_length=300)),
            ],
        ),
    ]
