from pathlib import Path
import os
from django.contrib.messages import constants as messages


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z7zpx!lgrqie$esczhb!yu1-ovoejlt@02very)5y*_ujbs(3k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', # 消さないとエラーなる
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diary',
    'accounts',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'private_diary.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'private_diary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'private_diary',
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST':'',
#         'PORT':'',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGGING={
    'version':1,
    'disable_existing_loggers':False,

    'loggers':{
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },
        
        'diary':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },

    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    }
}

SITE_ID = 1     #追加(必須)
# LOGIN_URL = 'login/' #追加

LOGIN_REDIRECT_URL ='diary:diary_list'
# LOGOUT_REDIRECT_URL = '/' #追加

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MESSAGE_TAGS = {
    messages.ERROR:'alert alert-danger',
    messages.WARNING:'alert alert-warning',
    messages.SUCCESS:'alert alert-success',
    messages.INFO:'alert alert-info',
}

AUTH_USER_MODEL = 'accounts.CustomUser'

AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ACCOUNT_AUTENICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True

LOGIN_REDIRECT_URL = 'diary:index'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

ACCOUNT_LOGOUT_ON_GET = True

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'