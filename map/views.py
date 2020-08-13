from django.shortcuts import render


# Create your views here.

def Sciences_Map_view(request):
    # page qu'on va chercher lors de la requête
    return render(request, 'map/map.html')


def Cyclotron_Map_view(request):
    # page qu'on va chercher lors de la requête
    return render(request, 'map/map.html')


def Lac_Map_view(request):
    # page qu'on va chercher lors de la requête
    return render(request, 'map/map.html')


def Jardin_botanique_Map_view(request):
    # page qu'on va chercher lors de la requête
    return render(request, 'map/map.html')


def Parc_Map_view(request):
    # page qu'on va chercher lors de la requête
    return render(request, 'map/map.html')


def Test_page(request):
    mapLac = "//umap.openstreetmap.fr/fr/map/carte-sans-nom_460975?scaleControl=true&miniMap=false&scrollWheelZoom" \
             "=true&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null" \
             "&embedControl=null&datalayersControl=true&onLoadPanel=none&captionBar=false&fullscreenControl=null" \
             "&locateControl=true "
    mapSciences = "..."
    mapCyclo = "..."
    mapBota = "..."
    mapParc = "..."

    return render(request, 'map/map.html')