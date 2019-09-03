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

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),# 自动文档
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search',include('haystack.urls')), # 全文检索框架
    url(r'^user/', include('user.urls',namespace='user')),  # 用户模块
    url(r'^article/', include('article.urls',namespace='article')),  # 文章模块
    url(r'^photo/', include('photo.urls',namespace='photo')),  # 照片模块
    url(r'mdeditor/', include('mdeditor.urls')), # markdown 模块
    url(r'^comments/', include('django_comments.urls')),
    url(r'^', include('article.urls',namespace='article')),  # 文章模块
    url(r'^', include('user.urls',namespace='user')), 
    url(r'^', include('card.urls',namespace='card')),  # 卡片模块
    url(r'^', include('notes.urls',namespace='notes')),
    # url(r'^', include('docs.urls',namespace='docs')),
    # url(r'^', include('wx.urls',namespace='weixin'))
    url(r'^api/', include('api.urls',namespace='api')),
]


from django.contrib.flatpages import views

urlpatterns += [
    url(r'^about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
    # path('license/', views.flatpage, {'url': '/license/'}, name='license'),
]
# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG is False:
#     urlpatterns += patterns( ' ',url(r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),) 
