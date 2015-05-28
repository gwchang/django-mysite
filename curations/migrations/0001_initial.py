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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('file_text', models.CharField(max_length=200)),
                ('title_text', models.CharField(max_length=200)),
                ('link_url', models.CharField(max_length=300)),
                ('price_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title_text', models.CharField(max_length=200)),
                ('author_text', models.CharField(max_length=200)),
                ('description_text', models.CharField(max_length=2000)),
                ('homepage_url', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='collection',
            field=models.ForeignKey(default=0, to='curations.Collection'),
        ),
    ]
