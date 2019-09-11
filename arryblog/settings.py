"""
Django settings for arryblog project.

Generated by 'django-admin startproject' using Django 2.2.5

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import socket
# 包含数据库信息和邮箱信息等隐私内容，不上传
from . import private as pr 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = pr.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
# 以当前IP来判断是否是线上环境决定DEBUG行为
IP = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
if IP == pr.SERVER_IP:
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.flatpages',
    'django.contrib.sites',
    
    'mdeditor', # markdown编辑器
    'haystack', # 全文检索框架

    'photo',    # 相册模块
    'article',  # 文章模块
    'user',     # 用户模块
    'card',     # 卡片应用
    'notes',    # 笔记应用
    'api',      # api接口

    'djcelery',
    'rest_framework',
    'django_filters',
    # 'tinymce',  # 富文本编辑器
    # 'django_comments',
)



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.admindocs.middleware.XViewMiddleware',#doc
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'arryblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'arryblog.wsgi.application'

# COMMENTS_APP = 'library'
# COMMENTS_ALLOW_PROFANITIES = True

# django-celery 相关配置
import djcelery
djcelery.setup_loader()
BROKER_URL  = "redis://localhost:6379/3"
CELERY_RESULT_BACKEND = "redis://localhost:6379/3"
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60*60*24
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'



SITE_ID = 1
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': pr.DATABASE_NAME,
        'USER': pr.DATABASE_USER,
        'PASSWORD': pr.DATABASE_PASSWORD,
        'HOST': pr.DATABASE_HOST,
        'PORT':pr.DATABASE_PORT,
    }
}

# django认证系统使用的模型类
AUTH_USER_MODEL='user.User'

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

# AUTHENTICATION_BACKENDS = [
#     'user.user_login_backend.EmailOrUsernameModelBackend',# 自定义的后端认证类
#     'django.contrib.auth.backends.ModelBackend',
# ]
    
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATIC_ROOT = '/var/www/arryblog/static'
# 富文本编辑器配置
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}

# 邮箱配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = pr.EMAIL_HOST
EMAIL_PORT = pr.EMAIL_PORT
#发送邮件的邮箱
EMAIL_HOST_USER = pr.EMAIL_HOST_USER
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = pr.EMAIL_HOST_PASSWORD
#收件人看到的发件人
EMAIL_FROM = pr.EMAIL_FROM

ADMINS = pr.ADMINS

# Django 的缓存配置
CACHES = {
    "default":{
        "BACKEND":"django_redis.cache.RedisCache",
        "LOCATION":"redis://localhost:6379",
        "OPTIONS":{
            "CLIENT_CLASS":"django_redis.client.DefaultClient"
        }
    }
}

# 缓存设置，开发环境用dummycache，就是实现了接口的假缓存
# CACHES = {
#     'default':{
#         'BACKEND':'django.core.cache.backends.dummy.DummyCache',
#     }
# }

# session配进缓存里面
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


# 配置登录url地址
LOGIN_URL='/login' 


# 设置django文件存储类
DEFAULT_FILE_STORAGE='utils.fdfs.storage.FDFSStorage'

# 设置fdfs使用的client.conf文件路径
FDFS_CLIENT_CONF = './utils/fdfs/client.conf'
# 设置Nginx服务器的ip和端口号
FDFS_URL_PREFIX = 'http://%s:8888/' % pr.SERVER_IP

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'



# 全文检索框架配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎
        # 'ENGINE':'haystack.backends.whoosh_backend.WhooshEngine',
        'ENGINE':'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR,'whoosh_index')
    }
}
# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR ='haystack.signals.RealtimeSignalProcessor'

# 指定搜索结果每页显示条数
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5



REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS':"rest_framework.versioning.URLPathVersioning",
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1'],
    'VERSION_PARAM': 'version',

    'DEFAULT_THROTTLE_CLASSES': [
        'api.throttling.AnonRateThrottle',
        'api.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        '_anon': '10/m',
        '_user': '20/m',
    },
}