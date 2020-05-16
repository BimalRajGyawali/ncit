from django.db import models

"""
    All the database entities of image_gallery are described in this module.
"""
class Image(models.Model):
    """
        Image model maps the image uploaded in gallery section to the database.
    """
    caption = models.CharField(max_length=100)
    img = models.ImageField(upload_to='uploads/')

    def __str__(self):
        """
         :return: Readable representation of image object
        """
        return f'{self.caption} Image'
