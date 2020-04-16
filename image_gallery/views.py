from django.shortcuts import render
from .models import Image


def gallery(request):
    images = Image.objects.all()
    return render(request, 'image_gallery/gallery.html', {'gallery': images})
