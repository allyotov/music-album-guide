from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework import status


from core.serializers import AlbumSerializer
from core.services import get_album_queryset, save_album


class AlbumViewSet(ListModelMixin, GenericAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        sort_field = self.request.query_params.get('sorting')
        return get_album_queryset(sorting=sort_field)

    def get(self, request):
        return self.list(request)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        save_album(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)