# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParametroApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('param_app_nombre', models.CharField(max_length=30)),
                ('param_app_desc', models.CharField(max_length=200)),
                ('param_app_valor', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextoHTML',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto_HTML_nombre', models.CharField(max_length=30)),
                ('texto_HTML_desc', models.CharField(max_length=200)),
                ('texto_HTML_valor', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
