from django.shortcuts import render, redirect
from django.urls import reverse

from accueil.models import Accueil
from django.http import HttpResponse
from .forms import *
from .models import GalleryPhotos


def accueil_index(request):
    # effectue une requete
    accueil = Accueil.objects.all()
    # send info to our template
    context = {'accueil': accueil}
    return render(request, 'accueil/index.html', context)


def accueil_detail(request, pk):
    accueil = Accueil.objects.get(pk=pk)
    context = {'accueil': accueil}
    return render(request, 'accueil/index_detail.html', context)


def gallery(request):
    if request.method == 'GET':
        GalleryPhoto = GalleryPhotos.objects.all()
        context = {'GalleryPhoto': GalleryPhoto}
        return render(request, 'accueil/gallery.html', context)


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
