from django.shortcuts import render
from .models import Notice
from academics.models import Program


side_bar_notices = Notice.get_notices_by_date(7)
programs = Program.objects.all()


def notice(request):
    return render(request, 'notices/notices-list.html',
                  {'notices': Notice.get_all_notices(),
                   'side_bar_notices': side_bar_notices,
                   'programs': programs
                   })


def single_notice(request, heading):
    return render(request, 'notices/notice.html',
                  {'notice': Notice.get_notice(heading),
                   'side_bar_notices': side_bar_notices,
                   'programs': programs
                   })
