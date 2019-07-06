from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField
from user.models import User
# Create your models here.
from mdeditor.fields import MDTextField

class Album(BaseModel):
    '''文章类型模型类'''
    name = models.CharField(max_length=20, verbose_name='相册名称')
    logo = models.CharField(max_length=20, verbose_name='Logo')
    disc = models.CharField(max_length=200, verbose_name='描述')
    thumbnail = models.ImageField(upload_to='photo', verbose_name='相册缩略图')

    class Meta:
        db_table = 'df_album'
        verbose_name = '相册'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Photo(BaseModel):
    '''文章模型类'''

    type = models.ForeignKey('Album', verbose_name='照片类型')
    user = models.ForeignKey('user.User', verbose_name='作者')
    image = models.ImageField(upload_to='photo', verbose_name='原图')
    title = models.CharField(max_length=40, verbose_name='照片标题')
    content = models.CharField(max_length=200, verbose_name='照片描述')
    view = models.IntegerField(default=1, verbose_name='访问量')
    like = models.IntegerField(default=1, verbose_name='点赞数')

    class Meta:
        db_table = 'df_photo'
        verbose_name = '照片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# class ArticleImage(BaseModel):
#     '''文章图片模型类'''
#     article = models.ForeignKey('Article', verbose_name='所属文章')
#     image = models.ImageField(upload_to='article', verbose_name='图片路径')

#     class Meta:
#         db_table = 'df_article_image'
#         verbose_name = '文章图片'
#         verbose_name_plural = verbose_name



# class IndexArticleBanner(BaseModel):
#     '''首页轮播商品展示模型类'''
#     sku = models.ForeignKey('Article', verbose_name='商品')
#     image = models.ImageField(upload_to='banner', verbose_name='图片')
#     index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

#     class Meta:
#         db_table = 'df_index_banner'
#         verbose_name = '首页轮播商品'
#         verbose_name_plural = verbose_name


# class Comment(BaseModel):
#     '''评论模型类'''
#     article = models.ForeignKey('Article', verbose_name='所评论文章')
#     user = models.ForeignKey('user.User', verbose_name='作者')
#     content = HTMLField(blank=True, verbose_name='评论内容')

#     class Meta:
#         db_table = 'df_comment'
#         verbose_name = "评论"
#         verbose_name_plural = verbose_name


# class IndexPromotionBanner(BaseModel):
#     '''首页促销活动模型类'''
#     name = models.CharField(max_length=20, verbose_name='活动名称')
#     url = models.CharField(max_length=20, verbose_name='活动链接')
#     image = models.ImageField(upload_to='banner', verbose_name='活动图片')
#     index = models.SmallIntegerField(default=0, verbose_name='展示顺序')

#     class Meta:
#         db_table = 'df_index_promotion'
#         verbose_name = "主页促销活动"
#         verbose_name_plural = verbose_name



# class Quote(object):
#     """每日一句"""
#     quote = models.CharField(max_length=200, verbose_name='名言')
#     translation = models.CharField(max_length=200, verbose_name='翻译')
#     source = models.CharField(max_length=20, verbose_name='出处')

#     class Meta:
#         db_table = 'df_quote'
#         verbose_name = '每日一句'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.quote