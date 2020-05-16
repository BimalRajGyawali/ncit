from django.contrib import admin
from .models import Program, Subject, Semester

"""
    Models Program, Subject, Semester are registered to admin site.
"""


admin.site.register(Program)
admin.site.register(Subject)
admin.site.register(Semester)