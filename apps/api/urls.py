from django.conf.urls import url, include
from rest_framework import routers
from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'groups', views.GroupViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^(?P<version>[v1|v2]+)/', include(router.urls)),
]