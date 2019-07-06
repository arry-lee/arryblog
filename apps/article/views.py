from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.cache import cache
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
            articles = Article.objects.filter(user_id=1).filter(is_delete=False)
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
            cache.set('index_page',context,60)
        # 尝试从缓存中获取数据
        # context = cache.get('index_page_data')

        # if context is None:
        #     print('设置缓存')
        #     # 缓存中没有数据
        #     # 获取商品的种类信息
        #     types = ArticleType.objects.all()

        #     # 获取首页轮播商品信息
        #     article_banners = IndexArticleBanner.objects.all().order_by('index')

        #     # 获取首页促销活动信息
        #     promotion_banners = IndexPromotionBanner.objects.all().order_by('index')

        #     # 获取首页分类商品展示信息
        #     for type in types: # ArticleType
        #         # 获取type种类首页分类商品的图片展示信息
        #         image_banners = IndexTypeArticleBanner.objects.filter(type=type, display_type=1).order_by('index')
        #         # 获取type种类首页分类商品的文字展示信息
        #         title_banners = IndexTypeArticleBanner.objects.filter(type=type, display_type=0).order_by('index')

        #         # 动态给type增加属性，分别保存首页分类商品的图片展示信息和文字展示信息
        #         type.image_banners = image_banners
        #         type.title_banners = title_banners

        #     context = {'types': types,
        #                'article_banners': article_banners,
        #                'promotion_banners': promotion_banners}
        #     # 设置缓存
        #     # key  value timeout
        #     cache.set('index_page_data', context, 3600)

        # # 获取用户购物车中商品的数目
        # user = request.user
        # cart_count = 0
        # if user.is_authenticated():
        #     # 用户已登录
        #     conn = get_redis_connection('default')
        #     cart_key = 'cart_%d'%user.id
        #     cart_count = conn.hlen(cart_key)

        # # 组织模板上下文
        # context.update(cart_count=cart_count)

        # 使用模板
        return render(request, 'index.html', context)


# /article/文章id
class DetailView(View):
    '''详情页'''
    def get(self, request, article_id):
        '''显示详情页'''
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            # 文章不存在
            return redirect(reverse('article:index'))

        # # 获取文章的分类信息
        # types = ArticleType.objects.all()

        # # 获取文章的评论信息
        # comments = Comment.objects.filter(sku=sku).exclude(comment='')

        # # 获取新品信息
        # new_skus = Article.objects.filter(type=sku.type).order_by('-create_time')[:2]

        # # 获取同一个SPU的其他规格商品
        # same_spu_skus = Article.objects.filter(article=sku.article).exclude(id=article_id)

        # # 获取用户购物车中商品的数目
        # user = request.user
        # cart_count = 0
        # if user.is_authenticated():
        #     # 用户已登录
        #     conn = get_redis_connection('default')
        #     cart_key = 'cart_%d' % user.id
        #     cart_count = conn.hlen(cart_key)

        #     # 添加用户的历史记录
        #     conn = get_redis_connection('default')
        #     history_key = 'history_%d'%user.id
        #     # 移除列表中的article_id
        #     conn.lrem(history_key, 0, article_id)
        #     # 把article_id插入到列表的左侧
        #     conn.lpush(history_key, article_id)
        #     # 只保存用户最新浏览的5条信息
        #     conn.ltrim(history_key, 0, 4)

        # 组织模板上下文

        article.html_content = markdown.markdown(article.content,
                                                extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc', ])

        context = {'article':article}



        # 使用模板
        return render(request, 'article/detail.html', context)


# /js/data.json
class JsonDate(View):
    """处理ajax发过来的请求"""
    def get(self, request):
        data = int(request.GET.get('a'))
        ret = {'msg':data}
        return JsonResponse(ret)


class EditView(View):
    def get(self, request):

        return render(request, 'article.html')
# # 种类id 页码 排序方式
# # restful api -> 请求一种资源
# # /list?type_id=种类id&page=页码&sort=排序方式
# # /list/种类id/页码/排序方式
# # /list/种类id/页码?sort=排序方式
# class ListView(View):
#     '''列表页'''
#     def get(self, request, type_id, page):
#         '''显示列表页'''
#         # 获取种类信息
#         try:
#             type = ArticleType.objects.get(id=type_id)
#         except ArticleType.DoesNotExist:
#             # 种类不存在
#             return redirect(reverse('article:index'))

#         # 获取商品的分类信息
#         types = ArticleType.objects.all()

#         # 获取排序的方式 # 获取分类商品的信息
#         # sort=default 按照默认id排序
#         # sort=price 按照商品价格排序
#         # sort=hot 按照商品销量排序
#         sort = request.GET.get('sort')

#         if sort == 'price':
#             skus = Article.objects.filter(type=type).order_by('price')
#         elif sort == 'hot':
#             skus = Article.objects.filter(type=type).order_by('-sales')
#         else:
#             sort = 'default'
#             skus = Article.objects.filter(type=type).order_by('-id')

#         # 对数据进行分页
#         paginator = Paginator(skus, 1)

#         # 获取第page页的内容
#         try:
#             page = int(page)
#         except Exception as e:
#             page = 1

#         if page > paginator.num_pages:
#             page = 1

#         # 获取第page页的Page实例对象
#         skus_page = paginator.page(page)

#         # todo: 进行页码的控制，页面上最多显示5个页码
#         # 1.总页数小于5页，页面上显示所有页面
#         # 2. 当前页是前3页，显示1-5页
#         # 3. 当前页是后3页，显示后5页
#         # 4. 其他情况，显示当前页的前两页，当前页，后两页

#         num_pages = paginator.num_pages
#         if num_pages < 5:
#             pages = range(1,num_pages+1)
#         elif page <=3:
#             pases = range(1, 6)
#         elif num_pages - page <= 2:
#             pages = range(num_pages-4,num_pages+1)
#         else:
#             pages = range(page-2, page+3)

#         # 获取新品信息
#         new_skus = Article.objects.filter(type=type).order_by('-create_time')[:2]

#         # 获取用户购物车中商品的数目
#         user = request.user
#         cart_count = 0
#         if user.is_authenticated():
#             # 用户已登录
#             conn = get_redis_connection('default')
#             cart_key = 'cart_%d' % user.id
#             cart_count = conn.hlen(cart_key)

#         # 组织模板上下文
#         context = {'type':type, 'types':types,
#                    'skus_page':skus_page,
#                    'new_skus':new_skus,
#                    'cart_count':cart_count,
#                    'pages':pages,
#                    'sort':sort}

#         # 使用模板
#         return render(request, 'list.html', context)



from django.views.generic import TemplateView, ListView

class AboutView(TemplateView):
    template_name = "about.html"

class MusicView(TemplateView):
    template_name = "music.html"

class ClockView(TemplateView):
    template_name = "clock.html"

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
   
    def head(self, *args, **kwargs):
        last_article = self.get_queryset().latest('create_time')
        response = HttpResponse('')
        # RFC 1123 date format
        response['Last-Modified'] = last_article.create_time.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response









