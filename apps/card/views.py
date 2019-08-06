from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.response import Response

from django import forms
from django.shortcuts import render


class SnippetForm(forms.ModelForm):
	class Meta:
		model = Snippet
		fields = ['question', 'code','output','reason']

class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	renderer_classes = [JSONRenderer]


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer

	renderer_classes = [JSONRenderer,TemplateHTMLRenderer]

	def get(self,request,*args,**kwargs):
		self.object = self.get_object()
		print(request.accepted_renderer.format)
		print(request.accepted_media_type)

		if request.accepted_renderer.format == 'html':
			return render(request,'card/snippet_detail.html',{'snippet':self.object})
		else:
			serializer = SnippetSerializer(instance=self.object)
			data = serializer.data
			# content 返回的是json字符串,ajax 还要解析
			# data 返回的是 json 对象,ajax 直接取属性
			# content = JSONRenderer().render(serializer.data)
			return Response(data)
		
			# return Response({'snippet':self.object}, template_name = 'card/snippet_detail.html')
		

