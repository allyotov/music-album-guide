import logging

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from core.models import Album


from core.serializers import AlbumSerializer
from core.services import get_album_queryset

class AlbumViewSet(ListModelMixin, GenericAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        sort_field = self.request.query_params.get('sorting')
        return get_album_queryset(sorting=sort_field)

    def get(self, request):
        return self.list(request)
