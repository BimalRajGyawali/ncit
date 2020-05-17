from django.contrib import admin
from .models import Program, Subject, Semester, Message

"""
    Models Program, Subject, Semester are registered to admin site.
"""

class MessageAdmin(admin.ModelAdmin):
    list_display = ['name','email','message','date']
    list_filter = ['date']


admin.site.register(Program)
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(Message, MessageAdmin)