from django.urls import path, re_path
from core.views import AlbumListFormView

urlpatterns = [
    path('main', AlbumListFormView.as_view())
]
