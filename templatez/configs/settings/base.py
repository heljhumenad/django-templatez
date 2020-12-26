import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files Path
STATIC_FILES_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)
)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Generate your own secret key https://miniwebtool.com/django-secret-key-generator/ 
SECRET_KEY = ''

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

ROOT_URLCONF = 'templatez.configs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(STATIC_FILES_PATH, "templates")],
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

WSGI_APPLICATION = 'templatez.configs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#database

DATABASE_NAME = ''
DATABASE_USERNAME = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
# configure your port base on your environment setup
DATABASE_PORT = ''

# LIST OF DATABASE ENGINE 
DB_SQLITE = 'django.db.backends.sqlite3'
DB_POSTGRES = 'django.db.backends.postgresql'
DB_MYSQL =  'django.db.backends.mysql'
DB_ORACLE = 'django.db.backends.oracle'

DATABASES = {
    'default': {
        'ENGINE': DB_SQLITE,
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_FILES_FINDER = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_ROOT = os.path.join(STATIC_FILES_PATH,"staticfiles")


# Add your custom static directory
STATICFILES_DIRS = [
    os.path.join(STATIC_FILES_PATH, "static"),
]

STATIC_URL = '/static/'

# Handle session cookies if you want to destory at browser close
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
