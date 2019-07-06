from django.contrib import admin
from django.core.cache import cache
# Register your models here.
from photo.models import Photo,Album


class BaseModelAdmin(admin.ModelAdmin):
	"""docstring for IndexPromotionBannerAdmin"""
	def save_model(self, request, obj, form, change):
		'''新增或更新表中的数据时调用'''
		super().save_model(request, obj, form, change)
		# 异步更新静态页面 防止管理页面卡顿
		# from celery_tasks.tasks import generate_static_index_html
		# generate_static_index_html.delay()
		# 清除首页的缓存数据
		cache.delete('photo_page')

	def delete_model(self, request, obj):
		'''新增或更新表中的数据时调用'''
		super().delete_model(request, obj)
		# 异步更新静态页面 防止管理页面卡顿
		# from celery_tasks.tasks import generate_static_index_html
		# generate_static_index_html.delay()
		# 清除首页的缓存数据
		cache.delete('photo_page')

class AlbumAdmin(BaseModelAdmin):
	pass

class PhotoAdmin(BaseModelAdmin):
	pass


admin.site.register(Album,AlbumAdmin)
admin.site.register(Photo,PhotoAdmin)

