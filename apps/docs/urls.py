from . import views
from django.conf.urls import url

urlpatterns = [
    url(
        r'^doc/',
        views.ModelIndexView.as_view(),
        name='docs-root',
    ),
]
