from django.contrib import admin
from .models import Student, StudentLogin


class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll', 'name', 'sem', 'phone', 'registered']

class StudentLoginAdmin(admin.ModelAdmin):
    list_display = ['password', 'student', 'email']


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentLogin, StudentLoginAdmin)