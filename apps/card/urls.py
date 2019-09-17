from django.urls import re_path, path

from card import views

app_name='card'

urlpatterns = [
    re_path(r'^snippets/$', views.SnippetList.as_view(),name="snippet-list"),
    re_path(r'^snippets/(?P<pk>\d+)/$',views.SnippetDetail.as_view(),name="snippet-detail"),
    re_path(r'^python/(?P<module>[a-zA-Z0-9\._]+)/$', views.module_detail, name='module-detail'),
    path('python/', views.module_list, name='module-list'),
    path('problems/<slug:slug>/',views.LeetCodeDetail.as_view(),name='problems-detail'),
    re_path(r'^problems/$',views.LeetCodeList.as_view(),name='problems-list'),
]