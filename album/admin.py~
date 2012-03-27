from django.contrib import admin
from cdealer.album.models import Album

class AlbumAdmin(admin.ModelAdmin):
    list_display=('name','artist','stock','release_date',)
    search_fields=('name',)
    list_filter=('release_date',)
    filter_horizontal=('category',)
    raw_id_fields=('artist',)

admin.site.register(Album,AlbumAdmin)
