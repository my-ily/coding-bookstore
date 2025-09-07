
# from pathlib import Path
# import os


from pathlib import Path
import os
import dj_database_url

# بناء مسار المشروع الأساسي
BASE_DIR = Path(__file__).resolve().parent.parent

# السرية وDebug
SECRET_KEY = 'django-insecure-3xn46-)*_vqc=4$n6%_l%465)-z$m1@bywpz_!*(47%d^3+ks='
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# السماح بأي دومين (أو حطي الدومين حق Heroku عندك)
ALLOWED_HOSTS = ['bookstore11-bfaf954b9c6c.herokuapp.com', 'localhost', '127.0.0.1', '*']

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Bookstore1',
    'django_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # مهم للـ static files على Heroku
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# قواعد البيانات: نستخدم إعداد Heroku (DATABASE_URL) أولاً، وإذا غير موجود نرجع لـ Postgres محلي
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:1234@localhost:5432/bookdb'
    )
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# اللغة والوقت
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ملفات static
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# روابط تسجيل الدخول/الخروج
LOGIN_URL = '/auth_login'
LOGIN_REDIRECT_URL = 'AllBooks'
LOGOUT_REDIRECT_URL = 'login'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





import dj_database_url
import os

# إذا لم يكن موجودًا، تأكدي من تثبيت dj-database-url:
# pip install dj-database-url psycopg2-binary

# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get('DATABASE_URL')
#     )
# }

# للسماح لأي host
ALLOWED_HOSTS = ['bookstore11-bfaf954b9c6c.herokuapp.com', 'localhost', '127.0.0.1']

# لضمان عمل static files على Heroku
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'









import dj_database_url

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'django-insecure-3xn46-)*_vqc=4$n6%_l%465)-z$m1@bywpz_!*(47%d^3+ks='
# DEBUG = True


# ALLOWED_HOSTS = ['bookstore11-bfaf954b9c6c.herokuapp.com', 'localhost', '127.0.0.1']

# # Authentication URLs
# LOGIN_URL = '/auth_login'
# LOGIN_REDIRECT_URL = 'AllBooks'
# LOGOUT_REDIRECT_URL = 'login'

# # Installed apps
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'Bookstore1',
#     'django_bootstrap5',
# ]

# # Middleware
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # قبل الجلسات
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'config.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'config.wsgi.application'

# # Database (Heroku PostgreSQL)
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get('DATABASE_URL', f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
#     )
# }

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # Static files
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

