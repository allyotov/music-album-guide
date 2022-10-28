import logging
from django.views import View
from django.shortcuts import render


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

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
        albums = [
            {
                'name': 'Album 1',
                'artist': {'name': 'Artist 1'},
                'tracks': ['track1', 'track2', 'track3']
            }
        ]
        return render(request, 'core/albums.html', context={'albums': albums})

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
        return render(request, 'core/albums.html', context={'albums': albums})
