# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appConfig', '0003_remove_textohtml_texto_html_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='textohtml',
            name='texto_HTML_valor',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
