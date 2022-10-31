import logging
from django.views import View
from django.shortcuts import render
from rest_framework.exceptions import APIException
from core.services import get_albums

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class AlbumTableView(View):
    def get(self, request):
        try:
            albums = get_albums(sorting='artist')
            return render(request, 'core/albums.html', context={'albums': albums})
        except Exception as exc:
            return render(request, 'core/backend_error.html', context={'exc': exc})

    def post(self, request):
        sorting = request.POST.get('sort')
        if sorting:
            logger.debug(sorting)
        else:
            sorting = 'artist'
        try:
            albums = get_albums(sorting=sorting)
            return render(request, 'core/albums.html', context={'albums': albums})
        except Exception as exc:
            return render(request, 'core/backend_error.html', context={'exc': exc})
