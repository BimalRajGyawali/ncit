from django.db import models
from django.utils import timezone
from django.urls import reverse


class Notice(models.Model):
    heading = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100, default='NCIT')

    def get_absolute_url(self):
        return reverse('notice', args=(self.heading.replace(' ', '-'),))

    def __str__(self):
        return f'{self.heading}'

    @staticmethod
    def get_notices_by_date(n):
        return Notice.objects.all().order_by('-date_posted')[:n]

    @staticmethod
    def get_all_notices():
        return Notice.objects.all().order_by('-date_posted')


    @staticmethod
    def get_notice(heading):
        heading = heading.replace('-', ' ')
        return Notice.objects.filter(heading=heading).first()
