from django.shortcuts import render
from .models import Notice
from academics.models import Program
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


side_bar_notices = Notice.get_notices_by_date(7)
programs = Program.objects.all()


def notice(request):
    page_num = request.GET.get('page', 1)
    notices = Notice.get_all_notices()
    paginator = Paginator(notices, 8)  # 10 notices in one page
    print(page_num)
    try:
        notices = paginator.page(page_num)

    except PageNotAnInteger:
        notices = paginator.page(1)

    except EmptyPage:
        notices = paginator.page(paginator.num_pages)


    return render(request, 'notices/notices-list.html',
                  {'notices': notices,
                   'side_bar_notices': side_bar_notices,
                   'programs': programs
                   })


def single_notice(request, heading):
    return render(request, 'notices/notice.html',
                  {'notice': Notice.get_notice(heading),
                   'side_bar_notices': side_bar_notices,
                   'programs': programs
                   })
