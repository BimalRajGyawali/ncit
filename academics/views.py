from django.shortcuts import render
from .models import Program, Semester, Message
from .forms import ContactUsForm
from django.utils import timezone

"""
    This module contains the methods and classes to handle HTTPRequest and 
    generate appropriate HTTPResponse.
"""


def program(request, code):
    """
    :type request: HTTPRequest
    :param request: carries request info

    :type code: int
    :param code: program code

    -> filters out the program on the basis of given program code

    -> if no program exists with that code, return 404

    -> otherwise, render program.html with context current_program


    """
    current_program = Program.objects.get(code=code)

    if current_program is None:
        return render(request, 'academics/404.html', {'error': '404 Page Not Found '})


    return render(request, 'academics/program.html', {'current_program': current_program})


def index(request):
    """

    :type request: HTTPRequest
    :param request: carries request info
    :return: renders index.html

    """
    return render(request, 'academics/index.html')


def facility(request):
    """

        :type request: HTTPRequest
        :param request: carries request info
        :return: renders facilities.html

        """
    return render(request, 'academics/facilities.html')


def scholarship(request):
    """

        :type request: HTTPRequest
        :param request: carries request info
        :return: renders scholarship.html

        """
    return render(request, 'academics/scholarship.html')


def handle404(request):
    """

           :type request: HTTPRequest
           :param request: carries request info
           :return: renders 404.html

           """
    return render(request, 'academics/404.html', {'error': '404 Page Not Found'})


def contact_us(request):
    newform = ContactUsForm()
    if request.method=='POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.date = timezone.now()
            message.save()
            return render(request, 'academics/contact-us.html', {'success' : True,'form':newform})
        else:
            return render(request, 'academics/contact-us.html', {'form' : form})
    else:
        return render(request, 'academics/contact-us.html', {'form' : newform})

