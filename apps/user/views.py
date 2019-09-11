from .forms import RegisterForm, LoginForm
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout,get_user_model,REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render,redirect,get_object_or_404
# from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.views.generic import View
from itsdangerous import SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from user.models import User
from utils.mixin import LoginRequiredMixin
from utils.utils import get_md5
from .tasks import send_active_email
import logging
from django.core.cache import cache
logger = logging.getLogger(__name__)

# from celery_tasks.tasks import send_register_active_email

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'user/register.html'

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(False)
            user.is_active = False
            user.save(True)
            site = 'arrylee.com'
            sign = get_md5(get_md5(settings.SECRET_KEY + str(user.id)))

            path = reverse('user:result')
            url = "http://{site}{path}?type=validation&id={id}&sign={sign}".format(site=site, path=path, id=user.id,
                                                                                   sign=sign)

            content = """
                            <p>请点击下面链接验证您的邮箱</p>
    
                            <a href="{url}" rel="bookmark">{url}</a>
    
                            再次感谢您！
                            <br />
                            如果上面链接无法打开，请将此链接复制至浏览器。
                            {url}
                            """.format(url=url)
            send_active_email.delay(receiver=[user.email, ], subject='验证您的电子邮箱', content=content)

            url = reverse('user:result') + '?type=register&id=' + str(user.id)
            return HttpResponseRedirect(url)
        else:
            return self.render_to_response({
                'form': form
            })


class LogoutView(RedirectView):
    url = '/login/'

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        
        cache.clear()
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to is None:
            redirect_to = '/'
        kwargs['redirect_to'] = redirect_to

        return super(LoginView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form = AuthenticationForm(data=self.request.POST, request=self.request)

        if form.is_valid():
            
            if cache and cache is not None:
                cache.clear()
            logger.info(self.redirect_field_name)

            auth.login(self.request, form.get_user())
            return super(LoginView, self).form_valid(form)
            # return HttpResponseRedirect('/')
        else:
            return self.render_to_response({
                'form': form
            })

    def get_success_url(self):

        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to):
            redirect_to = self.success_url
        return redirect_to


def account_result(request):
    type = request.GET.get('type')
    id = request.GET.get('id')

    user = get_object_or_404(get_user_model(), id=id)
    logger.info(type)
    if user.is_active:
        return HttpResponseRedirect('/')
    if type and type in ['register', 'validation']:
        if type == 'register':
            content = '''
    恭喜您注册成功，一封验证邮件已经发送到您 {email} 的邮箱，请验证您的邮箱后登录本站。
    '''.format(email=user.email)
            title = '注册成功'
        else:
            c_sign = get_md5(get_md5(settings.SECRET_KEY + str(user.id)))
            sign = request.GET.get('sign')
            if sign != c_sign:
                return HttpResponseForbidden()
            user.is_active = True
            user.save()
            content = '''
            恭喜您已经成功的完成邮箱验证，您现在可以使用您的账号来登录本站。
            '''
            title = '验证成功'
        return render(request, 'user/result.html', {
            'title': title,
            'content': content
        })
    else:
        return HttpResponseRedirect('/')























# def send_register_active_email(to_email,username,token):
# 	'''发送激活邮件,这里没有用异步果然慢'''
# 	subject = '阿锐博客欢迎信息'
# 	message = ''
# 	sender = settings.EMAIL_FROM
# 	receiver = [to_email]
# 	html_message = """<h1>%s, 欢迎您成为阿锐博客注册会员</h1>请点击下面链接激活您的账户</h1> 
# 	<a href='http://127.0.0.1:8000/user/active/%s'>http://127.0.0.1:8000/user/active/%s</a>""" % (username,token,token)
# 	send_mail(subject, message, sender, receiver,html_message=html_message)


# class RegisterView(View):
# 	"""注册视图类"""
# 	def get(self,request):
# 		'''显示注册页面'''
# 		return render(request, 'user/register.html')

# 	def post(self,request):
# 		'''进行注册处理'''
# 		# 1.接受数据
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		email = request.POST.get('email')
# 		allow = request.POST.get('allow')
# 		# 2.行数据校验
# 		if not all([username,password,email]):
# 			return render(request,'user/register.html',{'errmsg':'数据不完整'})

# 		if allow != 'on':
# 			return render(request,'user/register.html',{'errmsg':'请同意条款'})

# 		# 校验用户名是否重复
# 		try:
# 			user = User.objects.get(username=username)
# 		except User.DoesNotExist:
# 			user = None

# 		if user:
# 			return render(request, 'user/register.html',{'errmsg':'用户名已存在'})
		
# 		# 3.进行业务处理
# 		user = User.objects.create_user(username, email, password)
# 		user.is_active = 0
# 		user.save()
# 		# 发送激活邮件，包含激活链接：
# 		# 激活链接中需要包含用户的身份信息，并且加密
# 		# 加密使用 from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# 		# 生成激活token
# 		s = Serializer(settings.SECRET_KEY,3600)
# 		info = {'confirm':user.id}
# 		token = s.dumps(info)
# 		token = token.decode()
# 		# 发邮件 使用celery 将耗时任务放入队列
# 		send_register_active_email(email,username,token)
# 		# send_register_active_email.delay(email,username,token)
# 		# 4.返回应答
# 		return redirect(reverse('article:index'))

# class ActiveView(View):
# 	"""激活链接视图"""
# 	def get(self,request,token):
# 		'''进行用户激活'''
# 		# 进行解密，获取要激活的用户信息
# 		s = Serializer(settings.SECRET_KEY,3600)
# 		try:
# 			# 获取激活用户的id
# 			info = s.loads(token)
# 			user_id = info['confirm']
# 			# 根据 id 获取用户信息
# 			user = User.objects.get(id=user_id)
# 			user.is_active = 1
# 			user.save()
# 			# 跳转到登陆页面
# 			return redirect(reverse('user:login'))
# 		except SignatureExpired as e:
# 			# 激活链接过期
# 			return HttpResponse('激活链接已过期')

# class LoginView(View):
# 	"""docstring for LoginView"""
# 	def get(self,request):
# 		# 判断是否记住了用户名
# 		if 'username' in request.COOKIES:
# 			username = request.COOKIES.get('username')
# 			checked = 'checked'
# 		else:
# 			username = ''
# 			checked = ''
# 		return render(request,'user/login.html',{'username':username,'checked':checked})

# 	def post(self,request):
# 		username = request.POST.get('username')
# 		password = request.POST.get('password')
# 		print(username,password)
# 		if not all([username,password]):
# 			return render(request,'user/login.html',{'errmsg':'数据不完整'})

		
# 		user = authenticate(username=username,password=password)
# 		print(user)
# 		if user is not None:
# 			if user.is_active:
# 				# 记录用户登录状态
# 				s = login(request,user)
# 				print(user.is_authenticated)
# 				# 跳转到之前页面或者没有就跳到首页
# 				next_url = request.GET.get('next',reverse('article:index'))
# 				response = redirect(next_url)
# 				# 判断是否需要记住用户名
# 				remember = request.POST.get('remember')

# 				if remember == 'on':
# 					response.set_cookie('username',username, max_age=7*24*3600)
# 				else:
# 					response.delete_cookie('username')
# 				print(response)
# 				return response
# 			else:
# 				return render(request,'user/login.html',{'errmsg':'账户未激活'})
# 		else:
# 			return render(request,'user/login.html',{'errmsg':'用户名或密码错误'})

# # /user
# class UserInfoView(LoginRequiredMixin,View):
# 	'''用户中心-信息页'''
# 	def get(self,request):
# 		user = request.user
# 		context = {'user':user}
# 		return render(request,"user/user_center_info.html",context)

# # /user/logout
# class LogoutView(View):
# 	"""退出登录"""
# 	def get(self, request):
# 		# 清除用户的session信息
# 		logout(request)
# 		return redirect(reverse('article:index'))

