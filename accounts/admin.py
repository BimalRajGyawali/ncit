from django.contrib import admin
from .models import Student, StudentLogin


class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll', 'name', 'sem', 'phone','email', 'registered']

class StudentLoginAdmin(admin.ModelAdmin):
    list_display = ['password', 'student']


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentLogin, StudentLoginAdmin)