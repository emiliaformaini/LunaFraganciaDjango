# -*- coding: utf-8 -*-

"""
Django settings for LunaFraganciaDjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2obs4#a!@1vv^nusp%h#u9)7%h-ya1oj6h&p_gg12d6wi-em)*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

ADMINS = (
    (u'Fran', 'fransdelrio@gmail.com'),
    (u'Aromamania', 'aromamania.fragancias@gmail.com'),
)

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor', #ck-editor :)
    'contact_form', #django-contact-form
    'deployer', #guille Deployer
    #LunaFragancias apps
    'appConfig',
    'productos',
    'revendedores',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'LunaFraganciaDjango.urls'

WSGI_APPLICATION = 'LunaFraganciaDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MAQUETADO_ROOT = os.path.join(BASE_DIR, "maquetado")

######################################################################################################
# CK-Editor configuration by Guille.  DJANGO-CKEDITOR: https://github.com/shaunsephton/django-ckeditor
######################################################################################################
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo',
                '-', 'Bold', 'Italic', 'Underline',
                '-', 'Link', 'Unlink', 'Anchor',
                '-', 'Styles', 'Format',
                '-', 'TextColor', 'BGColor',
                '-', 'SpellChecker', 'Scayt',
                '-', 'Maximize',
            ],
            ['HorizontalRule',
                '-', 'Image', 'Iframe', 'Flash', 'Table',
                '-', 'BulletedList', 'NumberedList',
                '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
                '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
                '-', 'SpecialChar',
                '-', 'Source',
            ]
        ],
        'language': 'es',
        'scayt_sLang': 'es_ES',
        'wsc_lang': 'es_ES',
        'extraAllowedContent': 'iframe[src,width,height,frameborder,style]',
        'width': '100%',
    },
}

#CK-Editor vars.  DJANGO-CKEDITOR: https://github.com/shaunsephton/django-ckeditor
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "ckeditor-uploads/" #CK-Editor Upload path


######################################################################################################
# Email parameters. Guardar/obtener despues desde la Base de Datos.
######################################################################################################
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'aromamania.fragancias@gmail.com'  #'server.salida.mendoza'
# EMAIL_HOST_PASSWORD = 'cursoweb'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'aromamania.fragancias@gmail.com'


##################################################################################################
# Importar opciones de settings_local.py
##################################################################################################
try:
    from settings_local import *
except ImportError:
    pass



