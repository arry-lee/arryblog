from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions


class TokenAuthentication(BaseAuthentication):
	"""token"""
	def authenticate(self,request):
		token = request.query_params.get('token',None)
		if not token or token != "arrylee":
			raise exceptions.AuthenticationFailed('用户认证失败')

		if token == "arrylee":
			return ('管理员',token)

		# return ('登录用户',token)


	def authenticate_header(self,request):
		pass

