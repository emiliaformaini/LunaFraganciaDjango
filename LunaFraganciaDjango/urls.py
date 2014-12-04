# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os

from django.views.generic import TemplateView, RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LunaFraganciaDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #ck-editor
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.STATIC_ROOT}),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT}),

    url(r'^maquetado/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MAQUETADO_ROOT}, name='maquetado'),
    
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.STATIC_ROOT, 'css')}),

    url(r'^files/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.STATIC_ROOT, 'files')}),

    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.STATIC_ROOT, 'fonts')}),

    url(r'^imagenes/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.STATIC_ROOT, 'imagenes')}),

    url(r'^png/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.STATIC_ROOT, 'png')}),

    url(r'^js/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': os.path.join(settings.STATIC_ROOT, 'js')}),


    url(r'^ckeditor/', include('ckeditor.urls')),

	url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.STATIC_ROOT}),
	
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': settings.MEDIA_ROOT}),

    url(r'^contacto/', include('contact_form.urls')),
    url(r'^deployer/', include('deployer.urls')),

    url(r'^$', RedirectView.as_view(url='/maquetado/index.html', permanent=False)),

    
)


# Texto para poner al final del <title> de cada página. En la pestaña de la pagina.
admin.site.site_title = u'Administración del sitio Luna Fragancias'

# Texto a poner en los <h1> de todas las páginas.
admin.site.site_header = u'~ Administrador de Luna Fragancias ~'

# Texto a poner arriba de la página de index del admin
admin.site.index_title = u'Panel de control de Luna Fragancias'




