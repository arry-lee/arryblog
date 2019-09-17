from django.http import HttpResponse,Http404
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import hashlib
import requests
import xmltodict
import time
import json

from article.models import Article
TOKEN = 'helloarry'

def long2short(long_url,token="b1c8f57cf7f818f7d071788d0f2f95e6"):
	"""百度短链接服务"""  
	host = 'https://dwz.cn'
	path = '/admin/v2/create'
	url = host + path
	method = 'POST'
	content_type = 'application/json'
	 
	# TODO：设置待创建的长网址
	bodys = {'Url':long_url,'TermOfValidity':"1-year"}
	
	# 配置headers
	headers = {'Content-Type':content_type, 'Token':token}
	
	# 发起请求
	response = requests.post(url=url, data=json.dumps(bodys), headers=headers,verify=False)
	
	# 读取响应
	# print(response.text)
	# print(resp.text)
	short_url = json.loads(response.text)['ShortUrl']
	return short_url


class EchoView(View):
	message_types = ['text', 'image', 'voice', 'link', 'location', 'shortvideo','event']
	
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get(self,request):
		data = request.GET
		signature = data.get('signature')
		timestamp = data.get('timestamp')
		nonce = data.get('nonce')
		echostr = data.get('echostr')

		temp = [timestamp,nonce,TOKEN]
		temp.sort()
		temp = ''.join(temp)
		if (hashlib.sha1(temp.encode('utf-8')).hexdigest()==signature):
			return HttpResponse(echostr)
		else:
			return HttpResponse('vaild signature')
	


	def post(self,request):
		data = self.parse(request)
		return self.message_dispath(data)


	def parse(self,request):
		xml = request.body # 不是表单请求就要用body
		data = xmltodict.parse(xml)['xml']
		return data


	def message_dispath(self,data):
		if data['MsgType'].lower() in self.message_types:
			handler = getattr(self,data['MsgType'].lower(),self.message_type_not_allowed)
		else:
			handler = self.message_type_not_allowed
		return handler(data)

	def text(self,data):
		content = data['Content']

		if content.isdigit():
			try:
				a = Article.objects.get(id=int(content))
			except:
				pass
			else:
				content = a.title + ' www.arrylee.com' + a.get_absolute_url()
		elif content=="@":
			a = Article.objects.latest('create_time')
			content = a.title+ ' www.arrylee.com' + a.get_absolute_url()

		elif content=="#":
			a = Article.objects.latest('create_time')
			content = a.title+ ' www.arrylee.com' + a.get_absolute_url()

		else:
			try:
				from utils.translation import translate
				content = translate(content)
			except:
				pass

		resp = {
				'ToUserName':data.get('FromUserName'),
				'FromUserName':data.get('ToUserName'),
				'CreateTime':int(time.time()),
				'MsgType':'text',
				'Content': content,
			}

		xml = xmltodict.unparse({'xml':resp})
		return HttpResponse(xml)

	def image(self,data):
		picurl = data['PicUrl']

		content = "图片链接%s" %picurl
		
		resp = {
				'ToUserName':data.get('FromUserName'),
				'FromUserName':data.get('ToUserName'),
				'CreateTime':int(time.time()),
				'MsgType':'text',
				'Content': content,
			}

		xml = xmltodict.unparse({'xml':resp})
		return HttpResponse(xml)

	def voice(self,data):
		pass

	def link(self,data):
		title = data['Title']
		description = data['Description']
		url = data['Url']

		try:
			url = long2short(url)
		except:
			pass

		content = "%s%s%s" %(title,description,url)
		
		resp = {
				'ToUserName':data.get('FromUserName'),
				'FromUserName':data.get('ToUserName'),
				'CreateTime':int(time.time()),
				'MsgType':'text',
				'Content': content,
			}

		xml = xmltodict.unparse({'xml':resp})
		return HttpResponse(xml)

	def location(self,data):
		location_x = data['Location_X']
		location_y = data['Location_Y']
		# create_time = data["CreateTime"]
		content = "经度%s纬度%s" %(location_x,location_y)
		
		resp = {
				'ToUserName':data.get('FromUserName'),
				'FromUserName':data.get('ToUserName'),
				'CreateTime':int(time.time()),
				'MsgType':'text',
				'Content': content,
			}

		xml = xmltodict.unparse({'xml':resp})
		return HttpResponse(xml)


	def shortvideo(self,data):
		pass

	def event(self,data):
		# if data['Event'] == "location":
		# 	location_x = data['Latitude']
		# 	location_y = data['Longitude']
		# 	content = "经度%s纬度%s" %(location_x,location_y)
			
		if data['Event'] == "subscribe":
			content = "你好！我是阿锐，欢迎关注锐问,有什么要问的吗？另外，我的主页是 www.arrylee.com ，欢迎大家访问。"
		else:
			content = "Bye~"
		resp = {
				'ToUserName':data.get('FromUserName'),
				'FromUserName':data.get('ToUserName'),
				'CreateTime':int(time.time()),
				'MsgType':'text',
				'Content': content,
			}

		xml = xmltodict.unparse({'xml':resp})
		return HttpResponse(xml)

	def message_type_not_allowed(self,data):
		pass

		

