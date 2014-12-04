# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Revendedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('revend_apellido', models.CharField(max_length=60)),
                ('revend_nombre', models.CharField(max_length=60)),
                ('revend_tel2', models.CharField(max_length=30)),
                ('revend_tel1', models.CharField(max_length=30)),
                ('revend_email', models.EmailField(max_length=100)),
                ('revend_sitio_web', models.URLField()),
                ('revend_facebook', models.URLField()),
                ('revend_linkedin', models.URLField()),
                ('revend_observaciones', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
