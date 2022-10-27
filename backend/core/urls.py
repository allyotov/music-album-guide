from django.urls import path

# from core.api import ...ViewSet, ...
from core.views import index

urlpatterns = [
    # path('albums/', ...ViewSet.as_view(), name='albums_list'),
    path('test/', index, name='test'),
]