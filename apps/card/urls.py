from django.conf.urls import url

from card import views

app_name='card'

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(),name="snippet-list"),
    url(r'^snippets/(?P<pk>\d+)/$',views.SnippetDetail.as_view(),name="snippet-detail"),
    url(r'^python/(?P<module>[a-zA-Z0-9\._]+)/$', views.module_detail, name='module-detail'),
    url(r'^python/$', views.module_list, name='module-list'),
]