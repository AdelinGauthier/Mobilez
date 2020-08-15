from django.urls import path
from accueil import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # mobilez.be/accueil
    path('', views.accueil_index, name="accueil"),
    # mobilez.be/accueil/#numeroPK
    path("<int:pk>/", views.accueil_detail, name="accueil_detail"),
    path('gallery/', views.gallery, name="gallery"),
    path('addPicture/', views.addPicture, name="addPic"),
    path('success/', views.success, name="success"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
