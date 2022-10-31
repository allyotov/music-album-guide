from django.urls import path

from core.views import AlbumTableView

urlpatterns = [
    path('index', AlbumTableView.as_view(), name='index'),
]
