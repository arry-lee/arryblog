from django.shortcuts import render
from notes.models import Note
# from django.views.generic import ListView,CreateView,FormView
from utils.mixin import LoginRequiredMixin

# 应该同 REST api来写
# Create your views here.
from notes.serializers import NoteSerializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer,JSONRenderer
from rest_framework.response import Response

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
