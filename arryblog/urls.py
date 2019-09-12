"""arryblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),# 自动文档
    url(r'^admin/', admin.site.urls),
    url(r'^search',include('haystack.urls')), # 全文检索框架
    url(r'^photo/', include('photo.urls',namespace='photo')),  # 照片模块
    url(r'mdeditor/', include('mdeditor.urls')), # markdown 模块
    url(r'^comments/', include('django_comments.urls')),
    url(r'^', include('article.urls',namespace='article')),  # 文章模块
    url(r'^', include('user.urls',namespace='user')),  # 用户模块
    url(r'^', include('card.urls',namespace='card')),  # 卡片模块
    url(r'^', include('notes.urls',namespace='notes')),# 笔记模块
    url(r'^api/', include('api.urls',namespace='api')),
    url(r'^favicon\.ico$',RedirectView.as_view(url='static/favicon.ico'))
]




# 在此处添加静态页面
from django.contrib.flatpages import views
urlpatterns += [
    url(r'^about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
]

# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG is False:
#     urlpatterns += patterns( ' ',url(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),) 
