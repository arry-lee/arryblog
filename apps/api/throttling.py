from rest_framework.throttling import SimpleRateThrottle


class AnonRateThrottle(SimpleRateThrottle):
	scope = '_anon'

	def get_cache_key(self,request,view):
		# 用户已登录则跳过匿名频率限制
		if request.user:
			return None

		return self.cache_format % {
		'scope':self.scope,
		'ident':self.get_ident(request)
		}


class UserRateThrottle(SimpleRateThrottle):
	"""docstring for UserRateThrottle"""
	scope = '_user'

	def get_ident(self,request):
		return request.user

	def get_cache_key(self,request,view):
		# 用户未登录则跳过频率限制
		if not request.user:
			return None

		if request.user == "管理员":  #不用限制管理员
			return None
		return self.cache_format % {
		'scope':self.scope,
		'ident':self.get_ident(request)
		} 
		
"""settings
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'tpl.throttling.AnonRateThrottle',
        'tpl.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        '_anon': '10/m',
        '_user': '20/m',
    },
}
"""