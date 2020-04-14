from django.shortcuts import render
from .models import Image
from notices.models import Notice
from academics.models import Program


side_bar_notices = Notice.get_notices_by_date(7)
programs = Program.objects.all()



def gallery(request):
    images = Image.objects.all()
    return render(request, 'image_gallery/gallery.html',
                  {'gallery': images,
                   'side_bar_notices': side_bar_notices,
                   'programs': programs
                   })
