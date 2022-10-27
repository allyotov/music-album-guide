from cProfile import label
from core.models import Artist, Album, Track


def get_album_queryset(sorting: str = None):
    resulting_list = []
    sort_field = 'artist__name'
    if sorting == 'album':
        sort_field = 'name'
    for album in Album.objects.order_by(sort_field):
        item = dict()
        item['artist'] = album.artist.name
        item['name'] = album.name
        item['year'] = album.year
        item['tracks'] = Track.objects.all().filter(album=album).values_list('name', flat=True)
        resulting_list.append(item)

    return resulting_list
