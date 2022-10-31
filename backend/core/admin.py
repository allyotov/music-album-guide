from django.contrib import admin

from core.models import Album, Artist, Track


class ArtistAdmin(admin.ModelAdmin):
    fields = ('name',)

    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class AlbumAdmin(admin.ModelAdmin):
    fields = ('name', 'artist', 'year')

    list_display = ('name', 'artist', 'year')
    list_display_links = ('name',)
    search_fields = ('name', 'artist', 'year')
    list_filter = ('name', 'artist', 'year')


class TrackAdmin(admin.ModelAdmin):
    fields = ('name', 'album')

    list_display = ('name', 'album')
    list_display_links = ('name',)
    search_fields = ('name', 'album')
    list_filter = ('name', 'album')


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
