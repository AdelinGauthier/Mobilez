from django.contrib import admin
from .models import Accueil
from .models import GalleryPhotos


class AccueilAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume', 'description', 'map_url_data', 'image', 'qr_code')


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'images')


admin.site.register(Accueil, AccueilAdmin)
admin.site.register(GalleryPhotos, GalleryAdmin)
