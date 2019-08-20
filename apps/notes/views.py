from django.shortcuts import render
from django.http import JsonResponse
from notes.models import Note,Group,Tag
from django.views.generic import View
from utils.mixin import LoginRequiredMixin
from django.views.decorators.http import require_POST
# 应该同 REST api来写
# Create your views here.
from notes.serializers import NoteSerializer,GroupSerializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.response import Response
from user.tasks import send_email

from django.core.paginator import Paginator

PAZE_SIZE = 12


class NoteIndex(View):
	def get(self,request):
		group = request.GET.get('group',None)
		tag = request.GET.get('tag',None)

		groups = list(Group.objects.filter(parent=1))
		for g in groups:
			g.kids = Group.objects.filter(parent__name=g)

		tags = Tag.objects.all()
		
		if group=='trash':
			notes = Note.objects.filter(is_delete=True)
		else:
			notes = Note.objects.filter(is_delete=False)
			if group:
				notes = notes.filter(group__name=group)
			if tag:
				notes = notes.filter(tags__name=tag)

		paginator = Paginator(notes,PAZE_SIZE)
		page = request.GET.get('page') or 1
		notes = paginator.page(page)

		context = dict(groups=groups,tags=tags,notes=notes)
		context.update(title='笔记')

		return render(request,'notes/notes.html',context)


class NoteList(generics.ListCreateAPIView,LoginRequiredMixin):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer
	renderer_classes = [JSONRenderer]

	def perform_create(self, serializer):
		# print(self.request.POST.get('title'))
		# print(self.request.POST.get('content'))
		# print(serializer)

		try:
			g = Group.objects.get(id=1)# 必须要有一个group 不可为空
			serializer.save(owner=self.request.user,group=g)
		except Exception as e:
			print(e)
			raise e

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer
	renderer_classes = [JSONRenderer]


@require_POST
def contactme(request):
	subject = request.POST.get('subject','')
	content = request.POST.get('content','')
	sender = request.POST.get('email','匿名')
	if all([subject,content]):
		send_email.delay(subject=subject, content=content, sender=sender)
		return JsonResponse({'code':1,'msg':'发送成功'})
	else:
		return JsonResponse({'code':0,'msg':'数据不完整'})

'''应用使用了Restful 模式，其中有四个方法，GET 方法表示查看，POST 方法表
示创建，PUT 可以用于更新或者创建，DELETE 表示删除，其中POST 作用在一个
集合资源之上，而PUT 则是作用在一个具体资源之上，也就是说如果URL 在可以
在客户端确定就用PUT，如果在服务端确定就用POST 。视图中定义了一些函数用
来处理用户发出的请求，其中定义了GroupList 类用来处理用户发出的GET（查询）
和POST（创建）笔记本组的请求，GroupDetail 类用来处理用户发出的GET（查询）、
PUT （修改）、DELETE（删除）笔记的请求；定义NoteList 类处理用户GET（查询）
笔记本组下的笔记列表的请求；定义NoteDetail 类用来处理用户GET（查询）、PUT
（修改）、DELETE（删除）笔记的请求；定义NoteMetaDetail 类用来处理用户GET
（获取）笔记的时候得到笔记带的标签；定义NotePreviewDetail 类用来处理用户将
回收站中的笔记恢复的请求；定义NoteAutoAbstract 定义GET 方法获取笔记的摘要
信息。'''



class GroupList(generics.ListCreateAPIView,LoginRequiredMixin):
	"""用来获得所有的笔记本组信息或者创建一个新的笔记本组。

	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	renderer_classes = [JSONRenderer]

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


# class GroupDetail(View):
# 	"""用来获得所有的笔记本组信息或者创建一个新的笔记本组。

# 	"""
# 	def get(self,request):
# 		...

# 	def put(self,request):
# 		...

# 	def delete(self,request):
# 		...


# class NoteMetaDetail(object):
# 	"""用于对笔记本元信息进行查看"""
# 	def get(self,request):
# 		...


# class NotePreviewDetail(object):
# 	"""用于查看笔记本预览内容"""
# 	def get(self,request):
# 		...

		

# class NoteAutoAbstract(object):
# 	"""用于获得笔记本自动生成的摘要信息"""
# 	def get(self,request):
# 		...