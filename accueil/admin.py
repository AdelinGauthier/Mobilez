from django.contrib import admin
from .models import Accueil


class AccueilAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume', 'description', 'map_url_data', 'image', 'qr_code')


admin.site.register(Accueil, AccueilAdmin)
