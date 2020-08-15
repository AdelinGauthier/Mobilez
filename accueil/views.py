from django.shortcuts import render, redirect
from accueil.models import Accueil
from django.http import HttpResponse
from .forms import *


def accueil_index(request):
    # effectue une requete
    accueil = Accueil.objects.all()
    # send info to our template
    context = {
        'accueil': accueil
    }
    return render(request, 'accueil/index.html', context)


def accueil_detail(request, pk):
    accueil = Accueil.objects.get(pk=pk)
    context = {
        'accueil': accueil
    }
    return render(request, 'accueil/index_detail.html', context)


def gallery(request):
    return render(request, 'accueil/gallery.html')


def success(request):
    return render(request, 'accueil/success.html')

def addPicture(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = GalleryForm()
    return render(request, 'accueil/addPict.html', {'form': form})



