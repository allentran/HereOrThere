"""
Django settings for HereOrThere project.

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
SECRET_KEY = 'a!8611#vvvm(lo2gbhk)l648(um(vq8_w#$3oz@r#uo3cy8lm%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Facebook

FACEBOOK_APP_ID = '799986273348000'
FACEBOOK_APP_SECRET = '795662238ef28e0741ab4b7bdc1b9e7c'
FACEBOOK_PERMISSIONS = 'public_profile,user_birthday,user_location,user_education_history,user_friends'

# Instagram

IG_CLIENT_ID = '7ee1596fd66c4d9892a6f176fd6d8599'
IG_CLIENT_SECRET = '1eb95c8932af428b9b38753754b7bc30'

# FourSquare

FS_CLIENT_ID = 'HGCO5PFRJKVUUJDFB4S2ICB23STSOHZDYH5SYHY1GAFR5ZSQ'
FS_CLIENT_SECRET = 'HJOBTZVHMYHJWLUVJREZ0OEM3BS1HME34T0TF14D1UEX1RQU'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'FBLogin',
    'Location',
    'SiteUsers',
    'south',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'HereOrThere.urls'

WSGI_APPLICATION = 'HereOrThere.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'HT_DB',
        'USER': 'root',
        'PASSWORD': '7djJjsUs',
    }
}


PROJECT_DIR = os.path.dirname(__file__) # this is not Django setting.
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"), 
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/login/'
