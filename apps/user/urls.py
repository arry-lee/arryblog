from django.conf.urls import url
from django.contrib.auth import views as auth_view
# from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'user'

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(success_url='/'), name='login', kwargs={'authentication_form': LoginForm}),
    url(r'^register/$', views.RegisterView.as_view(success_url="/"), name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^user/result.html', views.account_result, name='result')
]

# from django.conf.urls import  url
# from user.views import RegisterView,LoginView,ActiveView,LogoutView,UserInfoView


# urlpatterns = [
# 	url(r'^register$', RegisterView.as_view(), name='register'),
# 	url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),
# 	url(r'^login$', LoginView.as_view(), name='login'),
# 	url(r'^logout$', LogoutView.as_view(), name='logout'), # 退出登录
# 	# url(r'^profile$', UserInfoView.as_view(), name='user'), # 用户中心-信息页
# ]
