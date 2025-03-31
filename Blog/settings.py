
from pathlib import Path
import os
import django
from django.utils.translation import gettext_noop
from django.conf import settings

from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hj@er$bzzi29zp=*bcv05@3^-)1ipgkkvcx1$sfz#d2m#&3^24'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simpleblog',
   
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
     'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates '],
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

WSGI_APPLICATION = 'Blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
        'default' : {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME' : 'db',
                'USER' : 'postgres',
                'PASSWORD': 'password',
                'HOST': 'localhost',
                'PORT': '5432', # default PostgreSQL port
        }
        }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
EXTRA_LANG_INFO = { 
    'am': { 
        'bidi': False, # left-to-right 
        'code': 'am', 
        'name': 'Amharic', 
        'name_local': u'አማሪኛ', #unicode codepoints here 
    }, 
 } 
 
LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO) 
django.conf.locale.LANG_INFO = LANG_INFO 
 
LANGUAGES = settings.LANGUAGES+ [('am', gettext_noop('Amharic')),]
from django.utils.translation import gettext_lazy as _

LOCALE_PATHS =(
     
     os.path.join(BASE_DIR ,'locale/'),
 )
LANGUAGES = [
    ('en', 'English'),
    
  
    ('am', 'Amharic'),
]
PARLE_LANGUAGES ={
    None:(
    
      
        {'code':'en',},
        {'code':'am',},
        
  
)
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/Media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'Media')

STATICFILES_DIR=[
    BASE_DIR / 'static',
]
LOCAL_PATH=[
    os.path.join(BASE_DIR, 'locale')
]
       
# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Or your email provider's SMTP server
EMAIL_PORT = 587  # Or your email provider's port
EMAIL_USE_TLS = True  # Or EMAIL_USE_SSL if required
EMAIL_HOST_USER = 'wondimagegnatr96@gmail.com'
EMAIL_HOST_PASSWORD = 'xqeg ojao owrg dlom'
DEFAULT_FROM_EMAIL = 'wondimagegnatr96@gmail.com' #This is the from email that will be used. 

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

