from typing import Dict, Any
import httpx
from httpx import ConnectError
from rest_framework.exceptions import APIException
ALBUMS_ENDPOINT = '/api/v1/albums/'


class MusicAlbumsGuideBackendClient:

    ok_status_code = 201
    timeout = 5

    def __init__(self, backend_url: str):
        self.url = '{0}{1}'.format(backend_url, ALBUMS_ENDPOINT)

    def get_albums(self, sorting: str) -> str:
        parameter = {'sorting': sorting}
        try:
            response = httpx.get(self.url, params=parameter)
        except ConnectError as exc:
            raise APIException(exc)
        response.raise_for_status()
        return response.json()

    def add(self, album_dict: Dict) -> str:
        response = httpx.post(self.url, json=album_dict)
        return response.json()