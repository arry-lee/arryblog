from rest_framework import serializers
from article.models import Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'color']

# class TagSerializer(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	name = serializers.CharField(max_length=20)
# 	color = serializers.CharField(max_length=20)


# 	def create(self, validated_data):
# 		"""
# 		创建并返回实例
# 		"""
# 		return Tag.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		"""
# 		更新并且返回存在的实例
# 		"""
# 		instance.name = validated_data.get('name',instance.name)
# 		instance.color = validated_data.get('color',instance.color)
# 		instance.save()
# 		return instance