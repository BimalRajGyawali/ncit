from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class Program(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    desc = models.TextField(default="")
    career_prospectus = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('programs', args=(self.code,))


class Subject(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    credit = models.IntegerField()
    programs = models.ManyToManyField(Program)

    def __str__(self):
        return f'{self.name}'


class Semester(models.Model):
    sem = models.IntegerField(
        validators=[
            MaxValueValidator(8),
            MinValueValidator(1)
        ])

    subjects = models.ManyToManyField(Subject)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)


    @staticmethod
    def get_meaningful_sem(sem):
        names = {
            1: "First (I)",
            2: "Second II",
            3: "Third (III)",
            4: "Fourth IV",
            5: "Fifth V",
            6: "Sixth VI",
            7: "Seventh VII",
            8: "Eight VIII"
        }
        return names.get(sem)


    def __str__(self):
        return f'{self.program} - {self.sem} sem'
