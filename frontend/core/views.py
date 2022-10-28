import logging
from django.views import View
from django.shortcuts import render


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


TEST_ALBUMS = [
    {
        'album': 'Album 1[1969]',
        'name': 'Album 1',
        'artist': {'name': 'Artist 1'},
        'tracks': ['track1', 'track2', 'track3']
    },
    {
        'album': 'Album 2[2015]',
        'name': 'Album 2',
        'artist': {'name': 'Artist 2'},
        'tracks': ['track1', 'track2', 'track3']
    },
    {
        'album': 'Album 3[1999]',
        'name': 'Album 3',
        'artist': {'name': 'Artist 3'},
        'tracks': ['track1', 'track2', 'track3']
    }
]
class AlbumListFormView(View):
    def get(self, request):
        # user_form = UserForm(instance=user)
        # context={'user_form': user_form, 'profile_id': profile_id}
        
        album_sorting = request.GET.get('album_sort_button')
        if album_sorting:
            logger.debug(album_sorting)
        
        artist_sorting = request.GET.get('artist_sort_button')
        if artist_sorting:
            logger.debug(artist_sorting)

        return render(request, 'core/albums.html', context={'albums': TEST_ALBUMS})

    def post(self, request):
        # user_form = UserForm(instance=user)
        # context={'user_form': user_form, 'profile_id': profile_id}
        logger.debug('POST method:')
        logger.debug(request.POST)
        album_sorting = request.POST.get('sort_by_album')
        if album_sorting:
            logger.debug(album_sorting)
        
        artist_sorting = request.POST.get('sort_by_artist')
        if artist_sorting:
            logger.debug(artist_sorting)
        albums = [
            {
                'name': 'Album 1',
                'artist': {'name': 'Artist 1'},
                'tracks': ['track1', 'track2', 'track3']
            }
        ]
        return render(request, 'core/albums.html', context={'albums': TEST_ALBUMS})
