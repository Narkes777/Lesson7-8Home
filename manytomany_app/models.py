from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    courses = models.ManyToManyField('Course')
    average_score = models.FloatField(null=True, blank=True)


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    average_score = models.FloatField(null=True, blank=True)
