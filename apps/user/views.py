

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
# from django.http import HttpResponse
from django.conf import settings
# from django.core.paginator import Paginator
from user.models import User

from django.views.generic import View
from utils.mixin import LoginRequiredMixin


from django.contrib.auth import authenticate, login, logout

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired

# from celery_tasks.tasks import send_register_active_email

# import re

# from django_redis import get_redis_connection

def send_register_active_email(to_email,username,token):
	'''发送激活邮件,这里没有用异步果然慢'''
	subject = '阿锐博客欢迎信息'
	message = ''
	sender = settings.EMAIL_FROM
	receiver = [to_email]
	html_message = """<h1>%s, 欢迎您成为阿锐博客注册会员</h1>请点击下面链接激活您的账户</h1> 
	<a href='http://127.0.0.1:8000/user/active/%s'>http://127.0.0.1:8000/user/active/%s</a>""" % (username,token,token)
	send_mail(subject, message, sender, receiver,html_message=html_message)


class RegisterView(View):
	"""注册视图类"""
	def get(self,request):
		'''显示注册页面'''
		return render(request, 'user/register.html')

	def post(self,request):
		'''进行注册处理'''
		# 1.接受数据
		username = request.POST.get('username')
		password = request.POST.get('pwd')
		email = request.POST.get('email')
		allow = request.POST.get('allow')
		# 2.行数据校验
		if not all([username,password,email]):
			return render(request,'user/register.html',{'errmsg':'数据不完整'})

		if allow != 'on':
			return render(request,'user/register.html',{'errmsg':'请同意条款'})

		# 校验用户名是否重复
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			user = None

		if user:
			return render(request, 'user/register.html',{'errmsg':'用户名已存在'})
		
		# 3.进行业务处理
		user = User.objects.create_user(username, email, password)
		user.is_active = 0
		user.save()
		# 发送激活邮件，包含激活链接：
		# 激活链接中需要包含用户的身份信息，并且加密
		# 加密使用 from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
		# 生成激活token
		s = Serializer(settings.SECRET_KEY,3600)
		info = {'confirm':user.id}
		token = s.dumps(info)
		token = token.decode()
		# 发邮件 使用celery 将耗时任务放入队列
		send_register_active_email(email,username,token)
		# send_register_active_email.delay(email,username,token)
		# 4.返回应答
		return redirect(reverse('article:index'))

class ActiveView(View):
	"""激活链接视图"""
	def get(self,request,token):
		'''进行用户激活'''
		# 进行解密，获取要激活的用户信息
		s = Serializer(settings.SECRET_KEY,3600)
		try:
			# 获取激活用户的id
			info = s.loads(token)
			user_id = info['confirm']
			# 根据 id 获取用户信息
			user = User.objects.get(id=user_id)
			user.is_active = 1
			user.save()
			# 跳转到登陆页面
			return redirect(reverse('user:login'))
		except SignatureExpired as e:
			# 激活链接过期
			return HttpResponse('激活链接已过期')

class LoginView(View):
	"""docstring for LoginView"""
	def get(self,request):
		# 判断是否记住了用户名
		if 'username' in request.COOKIES:
			username = request.COOKIES.get('username')
			checked = 'checked'
		else:
			username = ''
			checked = ''
		return render(request,'user/login.html',{'username':username,'checked':checked})

	def post(self,request):
		username = request.POST.get('username')
		password = request.POST.get('pwd')

		if not all([username,password]):
			return render(request,'user/login.html',{'errmsg':'数据不完整'})

		
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				# 记录用户登录状态
				login(request,user)
				# 跳转到之前页面或者没有就跳到首页
				next_url = request.GET.get('next',reverse('article:index'))
				response = redirect(next_url)
				# 判断是否需要记住用户名
				remember = request.POST.get('remember')

				if remember == 'on':
					response.set_cookie('username',username, max_age=7*24*3600)
				else:
					response.delete_cookie('username')
				return response
			else:
				return render(request,'user/login.html',{'errmsg':'账户未激活'})
		else:
			return render(request,'user/login.html',{'errmsg':'用户名或密码错误'})

# /user
class UserInfoView(LoginRequiredMixin,View):
	'''用户中心-信息页'''
	def get(self,request):
		user = request.user
		context = {'user':user}
		return render(request,"user/user_center_info.html",context)

# # /user/order
# class UserOrderView(LoginRequiredMixin,View):
# 	'''用户中心-订单页'''
# 	def get(self,request,page):
# 		'''获取用户订单信息'''
# 		user = request.user
# 		orders = OrderInfo.objects.filter(user=user)
# 		# 遍历获取商品信息
# 		for order in orders:
# 			# 根据 order_id 查询订单商品信息
# 			order_skus = OrderArticle.objects.filter(order_id = order.order_id)
# 			# 遍历order_skus 计算商品的小计
# 			for order_sku in order_skus:
# 				amount = order_sku.count * order_sku.price
# 				# 动态给order_sku 增加属性
# 				order_sku.amount = amount
# 			# 动态给order增加属性，保存订单信息
# 			order.skus = order_skus
# 			# 订单状态标题
# 			order.status_name = OrderInfo.ORDER_STATUS[order.order_status]
# 		# 分页
# 		paginator = Paginator(orders,1)
# 		# 处理页码

# 		# 获取第page页的内容
# 		try:
# 			page = int(page)
# 		except Exception as e:
# 			page = 1

# 		if page > paginator.num_pages:
# 			page = 1

# 		# 获取第page页的Page实例对象
# 		order_page = paginator.page(page)

# 		# todo: 进行页码的控制，页面上最多显示5个页码
# 		# 1.总页数小于5页，页面上显示所有页面
# 		# 2. 当前页是前3页，显示1-5页
# 		# 3. 当前页是后3页，显示后5页
# 		# 4. 其他情况，显示当前页的前两页，当前页，后两页

# 		num_pages = paginator.num_pages
# 		if num_pages < 5:
# 			pages = range(1,num_pages+1)
# 		elif page <=3:
# 			pases = range(1, 6)
# 		elif num_pages - page <= 2:
# 			pages = range(num_pages-4,num_pages+1)
# 		else:
# 			pages = range(page-2, page+3)

# 		context = {'order_page': order_page,
# 					'pages': pages,
# 					'page': 'order'
# 		}
		
# 		return render(request,'user_center_order.html',context)

# # /user/address
# class AddressView(LoginRequiredMixin,View):
# 	'''用户中心-地址页'''
# 	def get(self,request):
# 		# 获取登录用户对应的User对象
# 		user = request.user

# 		# 获取用户的默认收货地址
# 		try:
# 			address = Address.objects.get(user=user, is_defalut=True)
# 		except Address.DoesNotExist:
# 			address = None

# 		return render(request,'user_center_site.html',{'page':'address','address':address})

# 	def post(self,request):
# 		'''地址添加'''
# 		# 接受数据
# 		receiver = request.POST.get('receiver')
# 		addr = request.POST.get('addr')
# 		zip_code = request.POST.get('zip_code')
# 		phone = request.POST.get('phone')
# 		# 校验数据
# 		if not all([receiver,addr,phone]):
# 			return render(request,'user_center_site.html',{'errmsg':'数据不完整'})
# 		# 校验手机号
# 		if not re.match(r'1[3|4|5|7|8][0-9]{9}$',phone):
# 			return render(request, 'user_center_site.html',{'errmsg':'手机格式不对'})

# 		# 业务处理：地址添加
# 		user = request.user
# 		address = Address.objects.get_default_address(user)

# 		if address:
# 			is_default = False
# 		else:
# 			is_default = True
# 		# 添加地址
# 		Address.objects.create(user=user,
# 								receiver=receiver,
# 								addr=addr,
# 								zip_code=zip_code,
# 								phone=phone,
# 								is_defalut=is_default) # A typo in DB ignore
# 		# 返回应答
# 		return redirect(reverse('user:address'))
# # def send(request):
# # 	msg='<a href="http://www.seu.edu.cn" target="_blank">点击激活</a>'
# # 	send_mail('注册激活','',settings.EMAIL_FROM,['213131515@seu.edu.cn'],html_message=msg)
# # 	return HttpResponse('ok')

# /user/logout
class LogoutView(View):
	"""退出登录"""
	def get(self, request):
		# 清除用户的session信息
		logout(request)
		return redirect(reverse('article:index'))

# some_app/views.py
