# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appConfig', '0002_auto_20141111_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textohtml',
            name='texto_HTML_valor',
        ),
    ]
