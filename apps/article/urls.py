from django.conf.urls import url
from article.views import (IndexView, JsonDate, 
	AboutView,MusicView,ClockView,
	ArticleTypeList,ArticleTypeCreate, ArticleTypeUpdate,ArticleTypeDelete,
	ArticleDetail,ArticleList,ArticleCreate, ArticleUpdate, ArticleDelete,
	ArticleYearArchiveView,ArticleMonthArchiveView,ArticleDayArchiveView)


urlpatterns = [
	url(r'^js',JsonDate.as_view()),
	url(r'^about/$', AboutView.as_view(), name='about'), # 编辑文章页
	url(r'^list/$',ArticleList.as_view()),
	url(r'^music/$', MusicView.as_view(), name='about'), 
	url(r'^clock/$', ClockView.as_view(), name='clock'), 

	url(r'^atypes/$', ArticleTypeList.as_view(), name='atypes'), 
	url(r'^atypes/add/$', ArticleTypeCreate.as_view(), name='atypes-add'),
	url(r'^atypes/(?P<pk>\d+)/update$', ArticleTypeUpdate.as_view(), name='atypes-update'),
	url(r'^atypes/(?P<pk>\d+)/delete/$', ArticleTypeDelete.as_view(), name='atypes-delete'),

	url(r'^article/all/$', ArticleList.as_view(), name='article-list'),
	url(r'^article/(?P<pk>\d+)/$', ArticleDetail.as_view(), name='article-detail'),
	url(r'^article/add/$', ArticleCreate.as_view(), name='article-add'),
	url(r'^article/(?P<pk>\d+)/update/$', ArticleUpdate.as_view(), name='article-update'),
	url(r'^article/(?P<pk>\d+)/delete/$', ArticleDelete.as_view(), name='article-delete'),


	url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/',ArticleDayArchiveView.as_view(month_format='%m'),name="article_day_archive"),	
	url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/',ArticleMonthArchiveView.as_view(month_format='%m'),name="article_month_archive"),	
	url(r'^archive/(?P<year>\d{4})/',ArticleYearArchiveView.as_view(),name="article_year_archive"),
	url(r'^$', IndexView.as_view(), name='index'), # 首页
]