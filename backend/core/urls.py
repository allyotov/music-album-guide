from django.urls import path

from core.api import AlbumViewSet
from core.views import index

urlpatterns = [
    path('v1/albums/', AlbumViewSet.as_view(), name='albums_list'),
    path('test/', index, name='test'),
]
