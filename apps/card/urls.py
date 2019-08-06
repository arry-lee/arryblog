from django.conf.urls import url

from card import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(),name="snippet-list"),
    url(r'^snippets/(?P<pk>\d+)/$',views.SnippetDetail.as_view(),name="snippet-detail"),
]