from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('accueil/', include('accueil.urls')),
    path('map/', include('map.urls')),
]