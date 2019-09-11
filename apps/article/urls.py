from django.conf.urls import url
from article.views import (ArticleCreate, 
	ArticleDayArchiveView, ArticleDelete, ArticleDetail,ArticleList,
	ArticleMonthArchiveView, ArticleTypeCreate, ArticleTypeDelete,
	ArticleYearArchiveView, ArticleTypeList, ArticleTypeUpdate, ArticleUpdate, 
	IndexView,ArticleTypeDetail)

from article import views

app_name='article'

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'), # 首页
	url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/',ArticleDayArchiveView.as_view(month_format='%m'),name="article_day_archive"),
	url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/',ArticleMonthArchiveView.as_view(month_format='%m'),name="article_month_archive"),	
	url(r'^archive/(?P<year>\d{4})/',ArticleYearArchiveView.as_view(),name="article_year_archive"),
	
	url(r'^article/(?P<pk>\d+)/$', ArticleDetail.as_view(), name='article-detail'),
	url(r'^article/(?P<pk>\d+)/delete/$', ArticleDelete.as_view(), name='article-delete'),
	url(r'^article/(?P<pk>\d+)/update/$', ArticleUpdate.as_view(), name='article-update'),
	url(r'^article/add/$', ArticleCreate.as_view(), name='article-add'),
	url(r'^article/all/$', ArticleList.as_view(), name='article-list'),
	
	url(r'^atypes/$', ArticleTypeList.as_view(), name='atypes'), 
	url(r'^atypes/(?P<pk>\d+)/delete/$', ArticleTypeDelete.as_view(), name='atypes-delete'),
	url(r'^atypes/(?P<pk>\d+)/update$', ArticleTypeUpdate.as_view(), name='atypes-update'),
	url(r'^atypes/add/$', ArticleTypeCreate.as_view(), name='atypes-add'),
	
	url(r'^article/(?P<slug>[a-zA-Z]+)/$', ArticleTypeDetail.as_view(), name='articletype-detail'),
	url(r'^timeline/$', ArticleList.as_view(), name='article-list'),

]

