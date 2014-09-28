"""
Django settings for fabricCalc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '))53i)=pkz=3&k_$%%yste9d_590n3ar+0l^4uuvm8)u938-y('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fabric',
    'common',
    'smuggler',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fabricCalc.urls'

WSGI_APPLICATION = 'fabricCalc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if 'VCAP_SERVICES' in os.environ:
  import json
  vcap_services = json.loads(os.environ['VCAP_SERVICES'])
  mysql_srv = vcap_services['p-mysql'][0]
  cred = mysql_srv = mysql_srv['credentials']
  DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': cred['name'],
    'USER': cred['username'],
    'PASSWORD': cred['password'],
    'HOST': cred['hostname'],
    'PORT': cred['port'],
  }
}

else:
  DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": "db.sqlite3",
    "USER": "",
    "PASSWORD": "",
    "HOST": "",
    "PORT": "",
  }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
