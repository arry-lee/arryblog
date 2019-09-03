
from rest_framework import serializers

# 在这里实现Validator
# Validator 需要能调用，所以要实现 __call__ 方法
# 校验失败要抛出 ValidationError

class PasswordValidator(object):
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if value != self.base:
            message = 'This field must be %s.' % self.base
            raise serializers.ValidationError(message)

    def set_context(self, serializer_field):
        """
        This hook is called by the serializer instance,
        prior to the validation call being made.
        """
        # 执行验证之前调用,serializer_fields是当前字段对象
        pass


from user.models import User
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','gender']


from notes.models import Note,Group,Tag


class RecursiveField(serializers.Serializer):
    # 这个类代码保持不变
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class GroupSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='name')
    children = RecursiveField(many=True,read_only=True)
    class Meta:
        model = Group
        # depth = 1
        fields = ['id', 'label','children','parent']

from article.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'color']


class NoteSerializer(serializers.ModelSerializer):
    # group = GroupSerializer()
    class Meta:
        model = Note
        # depth = 1
        fields = ['id', 'title', 'content','is_delete','group','owner']