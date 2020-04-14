from django.db import models


class Image(models.Model):
    caption = models.CharField(max_length=100)
    img = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f'{self.caption} Image'
