from rest_framework import serializers

from core.models import Album, Artist, Track


class AlbumSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    year = serializers.IntegerField(required=True)
    artist = serializers.CharField(required=True)
    tracks = serializers.ListField(required=True)
