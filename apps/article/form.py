from .models import ArticleType
from django import forms

class ArticleTypeForm(forms.ModelForm):
	"""docstring for ArticleTypeForm"""
	class Meta:
		model = ArticleType
		field = ['name','logo']