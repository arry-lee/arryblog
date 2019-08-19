from django.http import HttpResponse,Http404
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import hashlib

import xmltodict
import time


from article.models import Article
TOKEN = 'helloarry'



class EchoView(View):
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
		xml = request.body # 不是表单请求就要用body
		req = xmltodict.parse(xml)['xml']
		msg_type = req.get('MsgType')


		if msg_type == 'text':
			query = req.get('Content')
			try:
				id_ = int(query)
				article = Article.objects.all().get(id=id_)
				content = article.content[:100]
			except:
				content = '内容不存在'

			resp = {
				'ToUserName':req.get('FromUserName'),
				'FromUserName':req.get('ToUserName'),
				'CreateTime':int(time.time()),
				'MsgType':'text',
				'Content': content,
			}

			xml = xmltodict.unparse({'xml': resp})
			return HttpResponse(xml)

		elif msg_type == 'image':
			pass

		elif msg_type == 'voice':
			pass
		"""
		<xml>
		  <ToUserName><![CDATA[toUser]]></ToUserName>
		  <FromUserName><![CDATA[fromUser]]></FromUserName>
		  <CreateTime>1351776360</CreateTime>
		  <MsgType><![CDATA[link]]></MsgType>
		  <Title><![CDATA[公众平台官网链接]]></Title>
		  <Description><![CDATA[公众平台官网链接]]></Description>
		  <Url><![CDATA[url]]></Url>
		  <MsgId>1234567890123456</MsgId>
		</xml>
		"""
		elif msg_type == 'link':
			pass

'''<xml>
  <ToUserName><![CDATA[toUser]]></ToUserName>
  <FromUserName><![CDATA[fromUser]]></FromUserName>
  <CreateTime>1351776360</CreateTime>
  <MsgType><![CDATA[location]]></MsgType>
  <Location_X>23.134521</Location_X>
  <Location_Y>113.358803</Location_Y>
  <Scale>20</Scale>
  <Label><![CDATA[位置信息]]></Label>
  <MsgId>1234567890123456</MsgId>
</xml>'''

		elif msg_type == 'location':
			pass

"""ToUserName	开发者微信号
FromUserName	发送方帐号（一个OpenID）
CreateTime	消息创建时间 （整型）
MsgType	小视频为shortvideo
MediaId	视频消息媒体id，可以调用获取临时素材接口拉取数据。
ThumbMediaId	视频消息缩略图的媒体id，可以调用获取临时素材接口拉取数据。
MsgId	消息id，64位整型"""

		elif msg_type == 'shortvideo':
			pass

		else:
			resp = {
				'ToUserName': req.get('FromUserName', ''),
				'FromUserName': req.get('ToUserName', ''),
				'CreateTime': int(time.time()),
				'MsgType': 'text',
				'Content': 'I LOVE YOU'
			}
			xml = xmltodict.unparse({'xml':resp})
			return HttpResponse(xml)

