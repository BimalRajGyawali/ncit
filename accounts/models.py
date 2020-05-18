from django.db import models

class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, unique=True)
    sem = models.IntegerField()
    registered = models.BooleanField(default=False)
    email = models.EmailField(default=None)

    def __str__(self):
        return self.name



class StudentLogin(models.Model):
    roll = models.IntegerField(unique=True)
    password = models.CharField(max_length=100)
    student = models.OneToOneField(on_delete=models.CASCADE)


    def __str__(self):
        return self.roll