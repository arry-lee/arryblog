from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# Create your models here.
import random
import datetime


class User(AbstractUser):
	GENDER_CHOICES = (
		('m', '男'),
		('f', '女'),
		('s', '密'),
	)
	nickname = models.CharField('昵称', max_length=100, blank=True)
	# source = models.ImageField('头像',storage=)
	slogon = models.CharField('slogon', max_length=100, blank=True)
	gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES, default='s')

	def __str__(self):
		return self.username

	class Meta:
		db_table = 'df_user'
		ordering = ['-id']
		verbose_name = '用户'
		verbose_name_plural = verbose_name
		get_latest_by = 'id'
			

from utils.db.base_model import BaseModel

class AddressManager(models.Manager):
	"""地址模型管理器"""
	# 1.改变原有查询的结果集:all
	# 2.封装方法:用户操作模型对应的数据表
	def get_default_address(self,user):
		try:
			address = self.get(user=user,is_defalut=True)
		except self.model.DoesNotExist:
			address = None
		return address
		
class Address(BaseModel):
	"""地址模型类"""
	user = models.ForeignKey('User', verbose_name='所属账户')
	receiver = models.CharField(max_length=20, verbose_name='收件人')
	addr = models.CharField(max_length=256, verbose_name='收件地址')	
	zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
	phone =models.CharField(max_length=11, verbose_name='联系电话')
	is_defalut = models.BooleanField(default=False, verbose_name='是否默认')

	# 自定义一个模型管理器对象
	objects = AddressManager()

	class Meta:
		db_table = 'df_address'
		verbose_name = '地址'
		verbose_name_plural = verbose_name


class Activity(models.Model):
	"""活动模型类"""
	ACTIVITY_CHOICES = (
				('#ebedf0','0'), 
				('#c6e48b','1'), 
				('#7bc96f','2'), 
				('#239a3b','3'),
				('#196127','4'),)

	user = models.ForeignKey('User', verbose_name='所属用户')
	activity_date = models.DateField(verbose_name='活动日期')
	activity_level = models.CharField(max_length=7,default='#ebedf0',choices=ACTIVITY_CHOICES,verbose_name='活动等级')

	def __str__(self):
		return str(self.user)+'__'+str(self.activity_date)+"__"+self.activity_level

	class Meta:
		db_table = 'df_activity'
		verbose_name = '活动表'
		verbose_name_plural = verbose_name

	
	@classmethod
	def fake_activity(cls,days,user_id=1):
		LEVEL = ['#ebedf0', '#c6e48b', '#7bc96f','#239a3b','#196127']
		end = datetime.datetime.today()
		for i in range(days):
			date = end - datetime.timedelta(days=i)
			user = User.objects.get(id=user_id)

			try:
				a = Activity.objects.get(activity_date=date,user=user)
			except:
				a = Activity()
				a.user = user
				a.activity_date = date 

			a.activity_level = random.choice(LEVEL)
			a.save()
