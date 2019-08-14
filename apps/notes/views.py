from django.shortcuts import render
from django.http import JsonResponse
from notes.models import Note
# from django.views.generic import ListView,CreateView,FormView
from utils.mixin import LoginRequiredMixin
from django.views.decorators.http import require_POST
# 应该同 REST api来写
# Create your views here.
from notes.serializers import NoteSerializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.response import Response
from user.tasks import send_email


class NoteList(generics.ListCreateAPIView,LoginRequiredMixin):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer
	renderer_classes = [JSONRenderer]

	def perform_create(self, serializer):
		print(self.request.POST)
		serializer.save(owner=self.request.user)

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