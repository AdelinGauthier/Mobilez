from django.urls import path
from accueil import views

urlpatterns = [
    # mobilez.be/accueil
    path('', views.accueil_index, name="accueil"),
    # mobilez.be/accueil/#numeroPK
    path("<int:pk>/", views.accueil_detail, name="accueil_detail"),
]
