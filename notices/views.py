from django.shortcuts import render
from .models import Notice
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def notice(request):
    page_num = request.GET.get('page', 1)
    notices = Notice.get_notices_by_date()
    paginator = Paginator(notices, 3)  # 3 notices in one page

    try:
        notices = paginator.page(page_num)

    except PageNotAnInteger:
        notices = paginator.page(1)

    except EmptyPage:
        notices = paginator.page(paginator.num_pages)

    return render(request, 'notices/notices-list.html', {'notices': notices})


def single_notice(request, heading):
    return render(request, 'notices/notice.html', {'notice': Notice.get_notice(heading)})
