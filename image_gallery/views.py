from django.shortcuts import render
from .models import Image

"""
    This module contains the methods and classes to handle HTTPRequest and 
    generate appropriate HTTPResponse.
"""


def gallery(request):
    """

    :type request: HTTPRequest
    :param request: carries request info
    :return: renders gallery.html with all the images from Image table

    """
    images = Image.objects.all()
    return render(request, 'image_gallery/gallery.html', {'gallery': images})
