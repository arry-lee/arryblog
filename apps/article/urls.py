from django.conf.urls import url
from article.views import IndexView, DetailView, JsonDate, EditView, AboutView,ArticleListView,MusicView,ClockView



urlpatterns = [
	url(r'^article/(?P<article_id>\d+)$', DetailView.as_view(), name='detail'), # 详情页
	# url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'), # 列表页
	url(r'^js',JsonDate.as_view()),
	url(r'^edit$', EditView.as_view(), name='edit'), # 编辑文章页
	url(r'^about/$', AboutView.as_view(), name='about'), # 编辑文章页
	url(r'^list/$',ArticleListView.as_view()),
	url(r'^music/$', MusicView.as_view(), name='about'), 
	url(r'^clock/$', ClockView.as_view(), name='clock'), 

	#url(r'^explore$',ArticleListView.as_view()),
	url(r'^$', IndexView.as_view(), name='index'), # 首页

]