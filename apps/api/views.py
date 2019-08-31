from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .permissions import TempPermission
from .authentication import TokenAuthentication
from .serializers import NoteSerializer,UserSerializer,GroupSerializer
from notes.models import Note,Group
from user.models import User

# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


class StandardResultsSetPagination(PageNumberPagination):
	# 默认每页显示的数据条数
	page_size = 4
	# 获取URL参数中设置的每页显示数据条数
	page_size_query_param = 'page_size'

	# 获取URL参数中传入的页码key
	page_query_param = 'page'

	# 最大支持的每页显示的数据条数
	max_page_size = 4



class UserViewSet(ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class NoteViewSet(ModelViewSet):
	
	authentication_classes = [TokenAuthentication,]
	permission_classes = [TempPermission,]
	# throttle_classes = [UserRateThrottle, AnonRateThrottle, ]
	pagination_class = StandardResultsSetPagination

	queryset = Note.objects.all()
	serializer_class = NoteSerializer


	filter_backends = (SearchFilter,OrderingFilter)
	# filter_class = GoodsFilter
	search_fields = ('title','content')  # ?search=xxx
	ordering_fields = ('title',)		 # ?ordering=title&

class GroupViewSet(ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	authentication_classes = [TokenAuthentication,]
	pagination_class = StandardResultsSetPagination
	permission_classes = [TempPermission,]

	queryset = Group.objects.all()
	serializer_class = GroupSerializer
