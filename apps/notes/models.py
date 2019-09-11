"""
笔记模块划分为四个小的模块，分别为笔记操作、笔记分组、标签管理以及回
收站管理。其中笔记操作模块提供给用户的功能主要是笔记新建、笔记删除以及笔
记修改；笔记分组模块完成笔记移动以及新建和删除分组；标签管理模块为用户提
供笔记添加标签的功能，一个笔记可以对应多个标签，一个标签可以用于多个笔记，
笔记和标签是多对多的关系；回收站管理模块提供清空回收站和还原笔记的功能。
"""

from django.db import models
from user.models import User
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
	owner = models.ForeignKey('user.User', verbose_name='作者',on_delete=models.CASCADE)

	last_read = models.DateTimeField(auto_now=True,null=True)
	vote = models.IntegerField(default=0)
	is_public = models.BooleanField(default=False)
	group = models.ForeignKey('Group',related_name='notes',null=True,on_delete=models.CASCADE)
	tags = models.ManyToManyField('Tag',related_name='notes')

	class Meta:
		db_table = 'df_note'
		verbose_name = '笔记'
		verbose_name_plural = verbose_name

	def __str__(self):
		if self.title:
			return self.title +'>>>'+ self.content
		return self.conten


class Group(models.Model):
	name = models.CharField(max_length = 20)
	create_time = models.DateTimeField(auto_now_add=True)
	parent = models.ForeignKey('self',related_name='children',null=True,blank=True,on_delete=models.CASCADE)
	owner = models.ForeignKey('user.User',related_name='folders',on_delete=models.CASCADE)

	ROOT_NAME = 'root'
	TRASH_NAME = 'trash'

	def __str__(self):
		return self.name

class Tag(models.Model):
	"""docstring for Tag"""
	name = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey('user.User',on_delete=models.CASCADE)

	def __str__(self):
		return self.name