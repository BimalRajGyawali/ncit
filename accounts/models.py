from django.db import models

class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    sem = models.IntegerField()
    program = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    pic = models.ImageField(upload_to='uploads/accounts/', default='uploads/accounts/default.jpeg')
    registered = models.BooleanField(default=False)

    class Meta:
        ordering = ['roll']

    @property
    def first_name(self):
       return self.name.split(' ')[0]

    def __str__(self):
        return self.name



class StudentLogin(models.Model):
    password = models.CharField(max_length=100)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.student.name} {self.student.roll}'