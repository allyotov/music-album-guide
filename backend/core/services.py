from typing import List

from core.models import Album, Artist, Track
from core.serializers import AlbumInputSerializer


def get_album_queryset(sorting: str = None) -> List[dict]:
    resulting_list = []
    sort_field = 'artist__name'
    if sorting == 'album':
        sort_field = 'name'
    for album in Album.objects.order_by(sort_field):
        item = {}
        item['album'] = str(album)
        item['artist@name'] = album.artist.name
        item['name'] = album.name
        item['year'] = album.year
        item['tracks'] = Track.objects.all().filter(album=album).values_list('name', flat=True)
        resulting_list.append(item)

    return resulting_list


def save_album(serializer: AlbumInputSerializer):  # noqa: WPS210
    data = serializer.validated_data
    name = data['name']
    year = data['year']
    artist = data['artist']
    tracks = data['tracks']
    artist_obj, artist_created = Artist.objects.get_or_create(name=artist)

    album_obj, object_created = Album.objects.get_or_create(
        name=name,
        artist=artist_obj,
        year=year,
    )
    for track in tracks:
        Track.objects.get_or_create(name=track, album=album_obj)
