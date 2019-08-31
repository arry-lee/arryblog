from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.cache import cache
# from django.core.paginator import Paginator
from photo.models import Photo, Album
# from django_redis import get_redis_connection
from django.http import JsonResponse


# /photo
class PhotoView(View):
    '''首页'''
    def get(self, request):
        '''显示首页'''
        # 从缓存中获取
        context = cache.get('photo_page')
        # 如果缓存中没有
        if not context:
            photos = Photo.objects.all()
            albums = Album.objects.all()
            context = {
                'photos':photos,
                'albums':albums
            }
            # 设置缓存就不用经常查数据库了 key value timeout
            print("设置缓存")
            cache.set('photo_page',context,3600)
        # 使用模板
        return render(request, 'album/photo.html', context)

# /photo/1
class AlbumView(View):
    '''首页'''
    def get(self, request, album_id):
        '''显示首页'''
        # 从缓存中获取
        key = 'ablum%s_page' % album_id
        context = cache.get(key)
        # 如果缓存中没有
        if not context:
            photos = Photo.objects.filter(type__id=int(album_id))

            context = {
                'photos':photos,
            }
            # 设置缓存就不用经常查数据库了 key value timeout
            cache.set(key,context,3600)
        # 使用模板
        return render(request, 'album/album_detail.html', context)











