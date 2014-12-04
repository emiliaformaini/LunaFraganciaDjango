from django.db import models
from django import forms
from ckeditor.fields import RichTextField

# Create your models here.

class ParametroApp(models.Model):
	param_app_nombre = models.CharField(max_length=30)
	param_app_desc = models.CharField(max_length=200)
	param_app_valor = models.CharField(max_length=300)

	def __unicode__(self):              # __str__ en Python 3
		return self.param_app_nombre


class TextoHTML(models.Model):
	texto_HTML_nombre = models.CharField(max_length=30)
	texto_HTML_desc = models.CharField(max_length=200)
	texto_HTML_valor = RichTextField()
	
	def __unicode__(self):              # __str__ en Python 3
		return self.texto_HTML_nombre


