from django.db import models

class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    sem = models.IntegerField()
    registered = models.BooleanField(default=False)

    class Meta:
        ordering = ['roll']

    def __str__(self):
        return self.name



class StudentLogin(models.Model):
    password = models.CharField(max_length=100)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.student.name} {self.student.roll}'