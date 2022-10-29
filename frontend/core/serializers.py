from rest_framework import serializers


class AlbumSerializer(serializers.Serializer):
    album = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    tracks = serializers.ListField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['artist@name'] = serializers.CharField()
