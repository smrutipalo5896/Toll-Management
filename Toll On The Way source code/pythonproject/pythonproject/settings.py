"""
Django settings for pythonproject project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from django.core.mail.backends import smtp
from django.conf.global_settings import EMAIL_HOST,EMAIL_HOST_USER,\
EMAIL_HOST_PASSWORD,EMAIL_PORT,EMAIL_USE_TLS

TEMPLATE_LOADERS=( 'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',
  )

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'subhamsenapati40@gmail.com'
EMAIL_HOST_PASSWORD = 'subhapal@1234'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=ogkx3wa1c!(eg^hp1l3f43-jyt0g21^*&cmo+7z_(kq69r%iw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.43.111', '127.0.0.1', '192.168.43.1', '192.168.137.1']


# Application definition

INSTALLED_APPS = [
    'emp.apps.EmpConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contact',
    'profiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'pay',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pythonproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = (
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
)


WSGI_APPLICATION = 'pythonproject.wsgi.application'

TEMPLATE_DIRS=(
   os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),"static","templates"),
  '\Desktop\ppp\pythonproject\templates\admin'
  
    
    )
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
   # '/var/www/static/',
]
SITE_ID = 1
LOGIN_URL='/accounts/login/'
LOGIN_REDIRECT_URL='/profiles/'

ACCOUNT_AUTHENTICATION_METHOD ="username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET =False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL =LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL =None

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3
ACCOUNT_EMAIL_REQUIRED =False
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_EMAIL_SUBJECT_PREFIX ="My subject: "
ACCOUNT_DEFAULT_HTTP_PROTOCOL ="http"

ACCOUNT_LOGOUT_ON_GET =False
ACCOUNT_LOGOUT_REDIRECT_URL ="/"
ACCOUNT_SIGNUP_FORM_CLASS =None
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL =True
ACCOUNT_USER_MODEL_EMAIL_FIELD ="email"
ACCOUNT_USER_MODEL_USERNAME_FIELD ="username"

ACCOUNT_USERNAME_MIN_LENGTH =5
ACCOUNT_USERNAME_REQUIRED =True
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
ACCOUNT_PASSWORD_MIN_LENGTH = 6
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_cdn")
MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR),"media_cdn")

STRIPE_PUBLISHABLE_KEY='pk_test_ROvoTSeB3D7xgO4omHumkrdn'
STRIPE_SECRET_KEY='sk_live_nEtpB59Bhw9UHFtaM8i5Sgs5'
