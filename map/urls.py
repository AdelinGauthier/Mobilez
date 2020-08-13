from django.urls import path, include
from map import views

urlpatterns = [
    # mobilez.be/
    path('sciences/', views.Sciences_Map_view, name="sciences_map"),
    path('cyclotron/', views.Cyclotron_Map_view, name="cyclotron_map"),
    path('lac/', views.Lac_Map_view, name="lac_map"),
    path('jardin_botanique/', views.Jardin_botanique_Map_view, name="jardin_botanique_map"),
    path('parc/', views.Parc_Map_view, name="parc_map"),
]