from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField
from user.models import User
# Create your models here.
from mdeditor.fields import MDTextField

class Album(BaseModel):
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