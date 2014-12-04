# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20141106_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categ_prod',
            new_name='categ_producto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='linea_prod',
            new_name='linea_producto',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='producto_cod',
            new_name='producto_codigo',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='producto_desc',
            new_name='producto_descripcion',
        ),
    ]
