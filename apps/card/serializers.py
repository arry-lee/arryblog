from .models import Snippet
from rest_framework import serializers


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'question', 'code','output','reason', 'linenos', 'language', 'style']