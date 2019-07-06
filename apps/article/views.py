from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.cache import cache
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.core.paginator import Paginator
from article.models import Article, ArticleType
from user.models import User, Activity

# from django_redis import get_redis_connection
from django.http import JsonResponse

from utils.shanbay import get_quote
import datetime
import markdown

# # http://127.0.0.1:8000
class IndexView(View):
    '''首页'''
    def get(self, request):
        '''显示首页'''
        # 从一篇文章开始
        context = cache.get('index_page')
        if not context:
            articles = Article.objects.filter(user_id=1).filter(is_delete=False).order_by('-create_time')[:4]
            types = ArticleType.objects.all() 
            # 获取最近一年的活动
            activitys = Activity.objects.filter(user_id=1)[:364]
            # 获取每日一句


            try:
                date = datetime.datetime.today().strftime('%Y-%m-%d')
                content,translation,author = get_quote(date=date)
            except:
                content,translation,author = '','',''


            context = {
                'content':content,
                'translation':translation,
                'author':author,
                'articles':articles,
                'types':types,
                'activitys':activitys,
            }

            context['content'] = markdown.markdown(context['content'],
            extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'])

            cache.set('index_page',context,60)
        return render(request, 'index.html', context)


# /js/data.json
class JsonDate(View):
    """处理ajax发过来的请求"""
    def get(self, request):
        data = int(request.GET.get('a'))
        ret = {'msg':data}
        return JsonResponse(ret)


# ArticleType 相关视图
class ArticleTypeList(ListView):
    # model = ArticleType
    context_object_name = 'article_type_list'
    queryset = ArticleType.objects.filter(is_delete=False)


class ArticleTypeCreate(CreateView):
    model = ArticleType
    fields = ['name','logo']


class ArticleTypeUpdate(UpdateView):
    model = ArticleType
    fields = ['name','logo']


class ArticleTypeDelete(DeleteView):
    model = ArticleType
    success_url = '/article/atypes/'

# Article 相关视图
class ArticleList(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = 'articles'

class ArticleDetail(DetailView):
    model = Article
    # template_name = "article_detail.html" #加上就会找不到
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        # 将 md 转换为 html 显示
        context = super().get_context_data(**kwargs)
        context['article'].content = markdown.markdown(context['article'].content,
            extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'])
        return context

class ArticleCreate(CreateView):
    model = Article
    fields = ['type','user','tag','title','content']


class ArticleUpdate(UpdateView):
    model = Article
    fields = ['type','user','tag','title','content']

class ArticleDelete(DeleteView):
    model = Article
    success_url = '/article/'


from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView


class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "create_time"
    make_object_list = True
    allow_future = True
    allow_empty = True


class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "create_time"
    make_object_list = True
    allow_future = True
    allow_empty = True


class ArticleDayArchiveView(DayArchiveView):
    queryset = Article.objects.all()
    date_field = "create_time"
    allow_future = True
    make_object_list = True
    allow_empty = True


class AboutView(TemplateView):
    template_name = "about.html"

class MusicView(TemplateView):
    template_name = "music.html"

class ClockView(TemplateView):
    template_name = "clock.html"











