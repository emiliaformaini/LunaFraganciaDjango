from django.db import models

# Create your models here.

class LineaProducto(models.Model):
	linea_prod_nombre = models.CharField(max_length=200)
	linea_prod_desc = models.CharField(max_length=200)

	def __unicode__(self):              # __str__ en Python 3
		return self.linea_prod_nombre


class CategoriaProducto(models.Model):
	categ_prod_nombre = models.CharField(max_length=200)
	categ_prod_desc = models.CharField(max_length=200)

	def __unicode__(self):              # __str__ en Python 3
		return self.categ_prod_nombre


class Producto(models.Model):
	linea_producto = models.ForeignKey(LineaProducto) #Foreign Key a LineaProducto
	categ_producto = models.ForeignKey(CategoriaProducto) #Foreign Key a CategoriaProducto
	producto_codigo = models.IntegerField()
	producto_nombre = models.CharField(max_length=200)
	producto_simil = models.CharField(max_length=200)
	producto_descripcion = models.CharField(max_length=200)

	def __unicode__(self):              # __str__ en Python 3
		return self.producto_nombre


class ImagenProducto(models.Model):
	producto = models.ForeignKey(Producto)
	imagen = models.ImageField("ImagenDelProducto", upload_to="images/", blank=True, null=True)

	# def __unicode__(self):              # __str__ en Python 3
	# 	return self.???  //como hacer para obtener el nombre del archivo???



