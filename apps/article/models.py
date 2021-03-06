from django.db import models
from utils.db.base_model import BaseModel
from tinymce.models import HTMLField
from user.models import User
# Create your models here.
from mdeditor.fields import MDTextField
from django.urls import reverse

class ArticleType(BaseModel):
    '''文章类型模型类'''
    name = models.CharField(max_length=20, verbose_name='种类名称')
    logo = models.CharField(max_length=20, verbose_name='标识')
    # image = models.ImageField(upload_to='type', verbose_name='文章类型图片')

    class Meta:
        db_table = 'df_article_type'
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('article:atypes-update',kwargs={'pk':self.pk})

    def __str__(self):
        return self.name

class Tag(BaseModel):
    '''标签类'''
    name = models.CharField(max_length=20, verbose_name='标签名称')
    color = models.CharField(max_length=20, verbose_name='颜色')

    class Meta:
        db_table = 'df_tag'
        verbose_name = '标签类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(BaseModel):
    '''文章模型类'''

    type = models.ForeignKey('ArticleType', verbose_name='文章类型',on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', verbose_name='作者',on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', verbose_name='标签集')
    title = models.CharField(max_length=40, verbose_name='文章标题')
    content = MDTextField(blank=True, verbose_name='文章内容')
    view = models.IntegerField(default=1, verbose_name='访问量')
    like = models.IntegerField(default=1, verbose_name='点赞数')

    enable_comments = models.BooleanField(default=True,verbose_name='允许评论')
    is_public = models.BooleanField(default=True,verbose_name='是否公开')
    
    class Meta:
        db_table = 'df_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('article:article-detail',kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title



class ArticleImage(BaseModel):
    '''文章图片模型类'''
    article = models.ForeignKey('Article', verbose_name='所属文章',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article', verbose_name='图片路径')

    class Meta:
        db_table = 'df_article_image'
        verbose_name = '文章图片'
        verbose_name_plural = verbose_name

class Comment(BaseModel):
    '''评论模型类'''
    article = models.ForeignKey('Article', verbose_name='所评论文章',on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', verbose_name='作者',on_delete=models.CASCADE)
    content = HTMLField(blank=True, verbose_name='评论内容')

    class Meta:
        db_table = 'df_comment'
        verbose_name = "评论"
        verbose_name_plural = verbose_name

class Quote(models.Model):
    """每日一句"""
    date = models.DateField()
    quote = models.CharField(max_length=200, verbose_name='名言')
    translation = models.CharField(max_length=200, verbose_name='翻译')
    source = models.CharField(max_length=200, verbose_name='出处')

    class Meta:
        db_table = 'df_quote'
        verbose_name = '每日一句'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.quote


# 控制评论行为
from django_comments.moderation import CommentModerator, moderator
class ArticleModerator(CommentModerator):
    email_notification = True
    auto_close_field   = 'create_time'
    # Close the comments after 365 days.
    close_after        = 365
    enable_field = 'enable_comments'

moderator.register(Article, ArticleModerator)