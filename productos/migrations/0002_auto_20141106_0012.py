# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'ImagenDelProducto', blank=True)),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='categ_prod_id',
            new_name='categ_prod',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='linea_prod_id',
            new_name='linea_prod',
        ),
    ]
