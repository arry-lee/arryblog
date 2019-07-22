from django.contrib import admin
from django.core.cache import cache
# Register your models here.
from article.models import Article, Tag, Comment, ArticleType,Quote


class BaseModelAdmin(admin.ModelAdmin):
	"""docstring for IndexPromotionBannerAdmin"""
	def save_model(self, request, obj, form, change):
		'''新增或更新表中的数据时调用'''
		super().save_model(request, obj, form, change)
		# 异步更新静态页面 防止管理页面卡顿
		# from celery_tasks.tasks import generate_static_index_html
		# generate_static_index_html.delay()

		# 清除首页的缓存数据
		cache.delete('index_page')

	def delete_model(self, request, obj):
		'''新增或更新表中的数据时调用'''
		super().delete_model(request, obj)
		# 异步更新静态页面 防止管理页面卡顿
		# from celery_tasks.tasks import generate_static_index_html
		# generate_static_index_html.delay()
		# 清除首页的缓存数据
		cache.delete('index_page')

class ArticleTypeAdmin(BaseModelAdmin):
	pass

class ArticleAdmin(BaseModelAdmin):
	list_display = ('title', 'tag', 'type','create_time')
	list_filter = ['create_time']
	search_fields = ['title']
	
class TagAdmin(BaseModelAdmin):
	pass

class CommentAdmin(BaseModelAdmin):
	pass

class QuoteAdmin(BaseModelAdmin):
	pass

admin.site.register(ArticleType,ArticleTypeAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Quote,QuoteAdmin)

