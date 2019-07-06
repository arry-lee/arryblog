"""
Django settings for arryblog project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bga5t#n-a9=mx^glxprkc#16c#z*n_t%o8jiwh(y*i+h7c!xo$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce', # 富文本编辑器
    'mdeditor', # markdown编辑器
    'haystack', # 注册全文检索框架
    'photo', # 光影模块
    'article', # 文章模块
    'user', # 用户模块
    'library',# 书架模块
    'django_comments',
    'django.contrib.sites',
)

COMMENTS_APP = 'library'
COMMENTS_ALLOW_PROFANITIES = True

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

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


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'arryblog',
        'USER': 'root',
        'PASSWORD': 'lxrsql',
        'HOST': 'localhost',
        'PORT':3306,
    }
}

# django认证系统使用的模型类
AUTH_USER_MODEL='user.User'

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
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
#发送邮件的邮箱
EMAIL_HOST_USER = 'arry_lee@qq.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'cnxmlxpzadwrjbaa'
#收件人看到的发件人
EMAIL_FROM = '阿锐<arry_lee@qq.com>'


# # Django 的缓存配置
# CACHES = {
#     "default":{
#         "BACKEND":"django_redis.cache.RedisCache",
#         "LOCATION":"redis://127.0.0.1:6379/9",
#         "OPTIONS":{
#             "CLIENT_CLASS":"django_redis.client.DefaultClient"
#         }
#     }
# }

# 缓存设置，开发环境用dummycache，就是实现了接口的假缓存
CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.dummy.DummyCache',
    }
}

# session配进缓存里面
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


# 配置登录url地址
LOGIN_URL='/user/login' 


# 设置django文件存储类
DEFAULT_FILE_STORAGE='utils.fdfs.storage.FDFSStorage'

# 设置fdfs使用的client.conf文件路径
FDFS_CLIENT_CONF = './utils/fdfs/client.conf'
# 设置Nginx服务器的ip和端口号
FDFS_URL_PREFIX = 'http://192.168.134.130:8888/'

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

