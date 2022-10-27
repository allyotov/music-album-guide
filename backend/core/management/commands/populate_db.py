from pathlib import Path
import csv
import logging
from django.core.management.base import BaseCommand
from core.models import Artist, Album, Track

CURRENT_PATH = Path(__file__).parent
ARTISTS_CSV = CURRENT_PATH / 'artists.csv'
ALBUMS_CSV = CURRENT_PATH / 'albums.csv'
TRACKS_CSV = CURRENT_PATH / 'tracks.csv'


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


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
        f = open(ARTISTS_CSV)
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            artist = Artist.objects.get_or_create(name=row[0])[0]

    def populate_albums(self):
        f = open(ALBUMS_CSV)
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            artist = Artist.objects.get(name=row[1])
            album = Album.objects.get_or_create(name=row[0], artist=artist, year=int(row[2]))

    def populate_tracks(self):
        f = open(TRACKS_CSV)
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            artist = Artist.objects.get(name=row[0])
            album = Album.objects.get(name=row[1], artist=artist)
            track = Track.objects.get_or_create(name=row[2], album=album)