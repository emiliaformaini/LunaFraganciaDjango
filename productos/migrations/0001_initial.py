# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categ_prod_nombre', models.CharField(max_length=200)),
                ('categ_prod_desc', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LineaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linea_prod_nombre', models.CharField(max_length=200)),
                ('linea_prod_desc', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('producto_cod', models.IntegerField()),
                ('producto_nombre', models.CharField(max_length=200)),
                ('producto_simil', models.CharField(max_length=200)),
                ('producto_desc', models.CharField(max_length=200)),
                ('categ_prod_id', models.ForeignKey(to='productos.CategoriaProducto')),
                ('linea_prod_id', models.ForeignKey(to='productos.LineaProducto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
