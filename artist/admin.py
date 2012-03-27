from django.contrib import admin
from cdealer.artist.models import Artist

class ArtistAdmin(admin.ModelAdmin):
    list_display=('name','website','intro',)
    search_fields=('name',)
    fields=('photo','name','website','category','intro',)
    filter_horizontal=('category',)

admin.site.register(Artist,ArtistAdmin)
