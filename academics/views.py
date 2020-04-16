from django.shortcuts import render, redirect
from .models import Program, Subject, Semester


def program(request, code):

    current_program = Program.objects.filter(code=code).first()

    if current_program is None:
        return render(request, 'academics/error.html', {'error': '404 Page Not Found '})

    current_program_semesters = Semester.objects.filter(program__code=code)
    semesters = []

    for semester in current_program_semesters:
        semester_subject_dict = {'semester': semester, 'name': Semester.get_meaningful_sem(semester.sem),
                                 'subjects': semester.subjects.all()}
        semesters.append(semester_subject_dict)


    context = {
        'current_program': current_program,
        'semesters': semesters,
       }

    return render(request, 'academics/program.html', context)


def home(request):
    return render(request, 'academics/home.html')


def facility(request):
    return render(request, 'academics/facilities.html')


def scholarship(request):
    return render(request, 'academics/scholarship.html')


def error(request):
    return render(request, 'academics/error.html', {'error': '404 Page Not Found'})


def test(request):
    return render(request, 'academics/my_test.html')

