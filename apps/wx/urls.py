from django.conf.urls import url

from wx import views


app_name = 'wx'

urlpatterns = [
    url(r'^wx/$', views.EchoView.as_view(), name='echo'),
]