from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from django.conf import settings


class FDFSStorage(Storage):
	'''重写django的文件储存方案，fast dfs文件存储类
		使得网站后端文件储存使用fast DFS  和 nginx
	'''
	def __init__(self,client_conf=None,base_url=None):
		'''初始化'''
		if client_conf is None:
			client_conf = settings.FDFS_CLIENT_CONF
		self.client_conf =client_conf

		if base_url is None:
			base_url = settings.FDFS_URL_PREFIX
		self.base_url = base_url

	def _open(self, name, mode='rb'):
		'''打开文件使用'''
		pass

	def _save(self, name, content):
		'''保存文件使用'''
		# name 你选的上传文件的名字
		# content：包含你上传文件内容的FILE对象
		client = Fdfs_client(self.client_conf)

		# 上传文件内容
		res = client.upload_by_buffer(content.read())

		if res.get('Status') != 'Upload successed.':
			raise Exception('上传文件到fast dfs失败')

		# 获取返回文件的 id
		filename = res.get('Remote file_id')

		return filename

	def exists(self,name):
		return False

	def url(self,name):
		'''返回访问的文件url路径'''
		return self.base_url+name
