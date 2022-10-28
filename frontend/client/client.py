from typing import Dict, Any
import httpx

ALBUMS_ENDPOINT = '/api/v1/albums/'


class MusicAlbumsGuideBackendClient:

    ok_status_code = 201
    timeout = 5

    def __init__(self, backend_url: str):
        self.url = '{0}{1}'.format(backend_url, ALBUMS_ENDPOINT)

    def get_albums(self, sorting: str) -> str:
        parameter = {'sorting': sorting}
        response = httpx.get(self.url, params=parameter)
        response.raise_for_status()
        return response.json()

    def add(self, album_dict: Dict) -> str:
        response = httpx.post(self.url, json=album_dict)
        return response.json()