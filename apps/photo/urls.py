from django.conf.urls import url
from photo.views import PhotoView,AlbumView

urlpatterns = [
	url(r'^(?P<album_id>\d+)$', AlbumView.as_view(), name='album'), # 相册
	# url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'), # 列表页
	url(r'^$', PhotoView.as_view(), name='photo'), # 首页

]