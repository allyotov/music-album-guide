from django.db import models

TITLE_LEN_ALLOWED = 256
NAME_LEN_ALLOWED = 128


class Artist(models.Model):
    name = models.CharField(max_length=NAME_LEN_ALLOWED)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=TITLE_LEN_ALLOWED)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return '{0}[{1}]'.format(self.name, self.year)


class Track(models.Model):
    name = models.CharField(max_length=NAME_LEN_ALLOWED)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
