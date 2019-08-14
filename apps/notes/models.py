from django.db import models

# Create your models here.
# 笔记是对一段文字而言、包含：
# 被引用的文字、
# 笔记类型：划线、想法
# 笔记内容
# 笔记作者
# 源url
# 定位方式
class Note(models.Model):
	title = models.CharField(null=True,max_length = 100)
	content = models.TextField(blank = True,verbose_name='笔记内容')

	create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
	update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')
	is_delete = models.BooleanField(default=False,verbose_name='删除标记')
	owner = models.ForeignKey('user.User', verbose_name='作者')

	class Meta:
		db_table = 'df_note'
		verbose_name = '笔记'
		verbose_name_plural = verbose_name

	def __str__(self):
		if self.title:
			return self.title +'>>>'+ self.content
		return self.content