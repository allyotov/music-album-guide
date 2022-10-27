from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return '{}[{}]'.format(self.name, self.year)


class Track(models.Model):
    name = models.CharField(max_length=128)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
