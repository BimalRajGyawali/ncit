from django.shortcuts import render, redirect
from .models import Program, Subject, Semester
from notices.models import Notice

programs = Program.objects.all()
side_bar_notices = Notice.get_notices_by_date(7)


def program(request, code):

    current_program = Program.objects.filter(code=code).first()


    if current_program is None:
        return render(request, 'academics/error.html',
                      {'error': '404 Page Not Found ', 'programs': programs, 'side_bar_notices': side_bar_notices})

    current_program_semesters = Semester.objects.filter(program__code=code)
    semesters = []

    for semester in current_program_semesters:
        semester_subject_dict = {'semester': semester, 'subjects': semester.subjects.all()}
        semesters.append(semester_subject_dict)


    context = {
        'programs': programs,
        'current_program': current_program,
        'semesters': semesters,
        'side_bar_notices': side_bar_notices
    }

    return render(request, 'academics/program.html', context)


def home(request):

    context = {
        'programs': programs,
        'side_bar_notices': side_bar_notices
    }
    return render(request, 'academics/home.html', context)
