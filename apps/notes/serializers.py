from notes.models import Note,Group,Tag
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = ['id', 'title', 'content','is_delete']



class GroupSerializer(serializers.ModelSerializer):
	"""docstring for GroupSerializer"""
	class Meta:
		model = Group
		fields = ['id', 'name', 'parent','owner']
		

