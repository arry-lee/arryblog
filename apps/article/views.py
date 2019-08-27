# from django.core.paginator import Paginator
# from django_redis import get_redis_connection
from article.models import Article, ArticleType, Quote
from notes.models import Note

from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View,TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from itertools import chain
from user.models import User, Activity
from utils.mixin import LoginRequiredMixin
from utils.shanbay import get_quote
import datetime
import markdown
from django.core.paginator import Paginator
# # http://127.0.0.1:8000
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

import calendar
import datetime


from . import tasks




def get_last_monday(today):
    '''获取前一个周一'''
    oneday = datetime.timedelta(days = 1)
    m1 = calendar.MONDAY
    while today.weekday() != m1:
        today -= oneday
    last_monday = today
    return last_monday


class IndexView(View):
    '''首页'''
    # @method_decorator(cache_page(60 * 15))
    def get(self, request):
        '''显示首页'''
        # 如果是认证用户则显示自己的文章，否则显示管理员的文章
        # context = cache.get('index_page')
        if True:
            if request.user.is_authenticated():
                articles = Article.objects.filter(user_id=request.user.id).filter(is_delete=False).order_by('-create_time')
                # 用户文章数量不够则用管理员的文章补齐4个
                if len(articles)<4:
                    x = 4 - len(articles)
                    articles1 = Article.objects.filter(user_id=1).filter(is_delete=False).order_by('-create_time')[:x]
                    new_articles = chain(articles,articles1)
                else:
                    new_articles = articles[:4]
            else:
                articles = Article.objects.filter(user_id=1).filter(is_delete=False).order_by('-create_time')
                new_articles = articles[:4]
            types = ArticleType.objects.all()

            today = datetime.datetime.today()
            # 获取最近一年的活动
            
            user = request.user if request.user.is_authenticated() else 1

            activitys = cache.get('activitys')
            if not activitys:
                last_year = today - datetime.timedelta(days=359)#365-6
                last_year = get_last_monday(last_year)
                try:
                    a = Activity.objects.get(user=user,activity_date=today)
                except:
                    Activity.fake_activity(days=1)
                finally:
                    tomorrow = today + datetime.timedelta(days=1)
                    activitys = Activity.objects.filter(user=user,activity_date__range=(last_year,tomorrow)).order_by('activity_date')
                    cache.set('activitys',activitys,60*60*24)
            # 获取每日一句
            quote = cache.get('quote')
            if not quote:
                try:
                    quote = Quote.objects.get(date=today)
                except:
                    date = today.strftime('%Y-%m-%d')
                    content,translation,author = get_quote(date=date)
                    quote = Quote.objects.create(date=today,quote=content,translation=translation,source=author)
                    quote.save()
                cache.set('quote',quote,60*60*24)

            for a in articles:
                a.content = markdown.markdown(a.content,
                    extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc'])

            # 分页器，若是首页则激活动态这个panel,
            # 要是有 page 参数则是文章选项卡
            paginator = Paginator(articles,6)

            page = request.GET.get('page')
            if page is None:
                isindex = True
                page = 1
            else:
                isindex = False

            articles = paginator.page(page)

            page = int(page)
            # 显示前后5页
            a = paginator.num_pages
            if a <= 5:
                start = 1
                end = a
            else:
                if page < 5:
                    start = 1
                    end = 5
                elif page > a-5:
                    start = a-4
                    end = a
                else:
                    start = page-2
                    end = page+2
            page_list = list(range(start,end+1))

            # 统计新增文章数量
            article_counter = Article.objects.filter(create_time__gt = today).count()
            articletype_counter = ArticleType.objects.filter(create_time__gt = today).count()
            
            if request.user.is_authenticated():
                notes = Note.objects.filter(owner_id=request.user.id)[:5]
            else:
                notes = Note.objects.filter(owner_id=1)[:5]
            context = {
                'quote':quote,
                'new_articles':new_articles,
                'articles':articles,
                'isindex':isindex,
                'types':types,
                'activitys':activitys,
                'article_counter':article_counter,
                'articletype_counter':articletype_counter,
                'page_list':page_list,
                'notes':notes,
            }

            # cache.set('index_page',context,60)
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

# class ArticleTypeDetail(LoginRequiredMixin,DetailView):
class ArticleTypeDetail(DetailView):
    """某一类别的详情视图，
    显示该类别下面的所有文章
    """
    model = ArticleType
    slug_field = 'logo' # slug 参数对应的域 是SingleObjectMixin里面的

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        # 将查询集添加到上下文
        if self.request.user.is_authenticated():
            articles = Article.objects.filter(type=self.object).filter(user=self.request.user)
        else:
            articles = Article.objects.filter(type=self.object).filter(user_id=1)
        context['articles'] = articles
        return context

class ArticleTypeCreate(LoginRequiredMixin,CreateView):
    model = ArticleType
    fields = ['name','logo']
    success_url = '/article/atypes/'

class ArticleTypeUpdate(LoginRequiredMixin,UpdateView):
    model = ArticleType
    fields = ['name','logo']


class ArticleTypeDelete(LoginRequiredMixin,DeleteView):
    model = ArticleType
    success_url = '/article/atypes/'

from django.contrib.auth import get_user_model

# Article 相关视图
# class ArticleList(LoginRequiredMixin,ListView):
class ArticleList(ListView):
    # model = Article
    template_name = "article_list.html"
    context_object_name = 'articles'

    def get_queryset(self):
        # 动态构建query_set self.request.user
        if self.request.user.is_authenticated():
            return Article.objects.filter(user = self.request.user)
        else:
            # 没登录就显示我的文章
            return Article.objects.filter(user_id=1)
class ArticleDetail(DetailView):
    """
    Detail view for a article
    """
    model = Article
    # template_name = "article_detail.html" #加上就会找不到
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        # 将 md 转换为 html 显示
        context = super().get_context_data(**kwargs)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc'])

        context['article'].content = md.convert(context['article'].content)
        context['article'].toc = md.toc
        return context

class ArticleCreate(LoginRequiredMixin,CreateView):
    model = Article
    fields = ['title','type','tags','content','user']

    # user 设置为当前用户
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.request.user
        kwargs.update(
            {'initial': {'user': user}}
        )
        return kwargs

class ArticleUpdate(LoginRequiredMixin,UpdateView):
    model = Article
    fields = ['title','type','tags','content']

    # 更新的话一般user不用变
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     user = self.request.user
    #     if user:
    #         kwargs.update(
    #             {'initial': {'user': user}}  # 给表单的phase字段传递外键实例
    #         )
    #     return kwargs

class ArticleDelete(LoginRequiredMixin,DeleteView):
    model = Article
    success_url = '/article/'


from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView

# class ArticleYearArchiveView(LoginRequiredMixin,YearArchiveView):
class ArticleYearArchiveView(YearArchiveView):
    queryset = Article.objects.all()
    date_field = "create_time"
    make_object_list = True
    allow_future = True
    allow_empty = True


# class ArticleMonthArchiveView(LoginRequiredMixin,MonthArchiveView):
class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Article.objects.all()
    date_field = "create_time"
    make_object_list = True
    allow_future = True
    allow_empty = True

# class ArticleDayArchiveView(LoginRequiredMixin,DayArchiveView):
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

class ResumeView(TemplateView):
    template_name = "user/resume.html"


# # -------------------------------------------------
# # add REST view here
# # -------------------------------------------------

# # 不需要这些了
# # from django.http import HttpResponse, JsonResponse
# # from django.views.decorators.csrf import csrf_exempt

# from rest_framework.parsers import JSONParser
# from article.models import Tag
# from article.serializers import TagSerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(['GET','POST'])
# def tag_list(request):
#     """
#     list all tags,or create a new tag
#     """
#     if request.method == 'GET':
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags,many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def tag_detail(request,pk):
#     """
#     更新或者删除 tag
#     """
#     try:
#         tag = Tag.objects.get(pk=pk)
#     except Tag.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TagSerializer(tag)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TagSerializer(tag,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         tag.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# # 使用类视图
# from rest_framework.views import APIView
# from django.http import Http404

# class Taglist(APIView):
#     def get(self,request,format=None):
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags,many=True)
#         return Response(serializer.data)

#     def post(self,request,format=None):
#         serializer = TagSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class TagDetail(APIView):
#     """
#     Retrieve, update or delete a tag instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Tag.objects.get(pk=pk)
#         except Tag.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         tag = self.get_object(pk)
#         serializer = TagSerializer(tag)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         tag = self.get_object(pk)
#         serializer = TagSerializer(tag, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         tag = self.get_object(pk)
#         tag.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # 进一步使用通用视图
# from rest_framework import generics

# class TagList(generics.ListCreateAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# class TagDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


# # 使用视图集
# from rest_framework import viewsets
# # from rest_framework.decorators import action

# class TagViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.

#     Additionally we also provide an extra `highlight` action.
#     """
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#     #                       IsOwnerOrReadOnly]

#     # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
#     def color(self, request, *args, **kwargs):
#         tag = self.get_object()
#         return Response(tag.color)

#     # def perform_create(self, serializer):
#     #     serializer.save(owner=self.request.user)