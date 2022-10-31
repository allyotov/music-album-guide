import csv
import logging
import os
from pathlib import Path

from django.core.management.base import BaseCommand

from core.models import Album, Artist, Track

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

STAGE = os.environ.get('SOURCE_DATA')
logger.debug(STAGE)
if STAGE == 'local':
    PARENT_PATH = Path(__file__).parent.parent.parent.parent.parent  # noqa: WPS219
else:
    PARENT_PATH = Path(__file__).parent
logger.debug('PARENT_PATH: %s' % PARENT_PATH)

SOURCE_DATA_PATH = PARENT_PATH / 'source_data'
ARTISTS_CSV = SOURCE_DATA_PATH / 'artists.csv'
ALBUMS_CSV = SOURCE_DATA_PATH / 'albums.csv'
TRACKS_CSV = SOURCE_DATA_PATH / 'tracks.csv'


class Command(BaseCommand):
    help = 'Populates database from csv files;'

    def handle(self, *args, **kwargs):
        logger.info('Populating the database model Artist: in progress;')
        self.populate_artist()
        logger.info('Populating the database model Artist: complete;')
        logger.info('Populating the database model Albums: in progress;')
        self.populate_albums()
        logger.info('Populating the database model Albums: complete;')
        logger.info('Populating the database model Tracks: in progress;')
        self.populate_tracks()
        logger.info('Populating the database model Tracks: complete;')

    def populate_artist(self):
        with open(ARTISTS_CSV) as artist_file:
            reader = csv.reader(artist_file, delimiter=';')
            for row in reader:
                Artist.objects.get_or_create(name=row[0])[0]

    def populate_albums(self):
        with open(ALBUMS_CSV) as album_file:
            reader = csv.reader(album_file, delimiter=';')
            for row in reader:
                artist = Artist.objects.get(name=row[1])
                Album.objects.get_or_create(name=row[0], artist=artist, year=int(row[2]))

    def populate_tracks(self):
        with open(TRACKS_CSV) as track_file:
            reader = csv.reader(track_file, delimiter=';')
            for row in reader:
                artist = Artist.objects.get(name=row[0])
                album = Album.objects.get(name=row[1], artist=artist)
                Track.objects.get_or_create(name=row[2], album=album)
