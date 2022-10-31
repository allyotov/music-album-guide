import logging
from typing import Dict, List

from rest_framework.exceptions import APIException

from client.client import MusicAlbumsGuideBackendClient as Client
from core.serializers import AlbumSerializer
from frontend.settings import BACKEND_URL

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_albums(sorting=None) -> List[Dict]:
    albums_client = Client(BACKEND_URL)

    try:
        content_json = albums_client.get_albums(sorting=sorting)
    except APIException:
        raise APIException('Нет ответа от бэкенда.')

    serializer = AlbumSerializer(data=content_json, many=True)
    if not serializer.is_valid():
        logger.debug(content_json)
        logger.debug(serializer.errors)
        raise APIException('API бэкенда вернул некорректные данные.')
    return serializer.validated_data
