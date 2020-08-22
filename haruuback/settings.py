import os

# Django settings
DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'q_=xlz4y^_52wipzpsifn3yz+g*t-%#p4o0obiw*)lx3rkdmz&'
ROOT_URLCONF = 'haruuback.urls'
WSGI_APPLICATION = 'haruuback.wsgi.application'
LANGUAGE_CODE = 'ja'
STATIC_URL = '/static/'
AUTH_USER_MODEL = 'accounts.HaruuUser'
TIME_ZONE = 'Asia/Tokyo'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
USE_TZ = True
USE_I18N = True
USE_L10N = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    # Local apps
    'api',
    'accounts',

    # Third party apps
    'rest_framework',
    'rest_auth',
    'corsheaders',

    # Django apps
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
    'corsheaders.middleware.CorsMiddleware',
]
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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'haruuback',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
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

# Django Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'api.authentication.CustomTokenAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
}
REST_AUTH_TOKEN_MODEL = 'accounts.models.CustomToken'
REST_AUTH_TOKEN_CREATOR = 'common.utils.custom_update_create_auth_token'
LOGIN_SERIALIZER = 'accounts.serializers.CustomLoginSerializer'
REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'accounts.serializers.CustomLoginSerializer',
}
CORS_ORIGIN_WHITELIST = (
    'http://192.168.0.7',
)
