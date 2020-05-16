from django.contrib import admin

from .models import Notice


"""
    Notice model registered to admin site.
"""
admin.site.register(Notice)
