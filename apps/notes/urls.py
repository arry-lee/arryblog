from django.conf.urls import url

from notes import views

app_name = "notes"

urlpatterns = [
	url(r'^notes/$', views.NoteList.as_view(),name="note-list"),
	url(r'^notes/(?P<pk>\d+)/$',views.NoteDetail.as_view(),name="note-detail"),
]