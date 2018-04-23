from django.db import models
from django.contrib.auth.models import User

class Profile(User):
    is_student = models.BooleanField(default = False)
    is_company = models.BooleanField(default = False)
    name = models.CharField(max_length = 255)

# Related to Student
class Education(models.Model):
    student = models.ForeignKey(Profile, on_delete = models.CASCADE)
    college = models.CharField(max_length=200)
    gpa = models.IntegerField()
    degree = models.CharField(max_length = 255)

class WorkEx(models.Model):
    student = models.ForeignKey(Profile, on_delete = models.CASCADE)
    company = models.CharField(max_length=200)  
    description = models.TextField()

# Related to company
class Internship(models.Model):
    company = models.ForeignKey(Profile, on_delete = models.CASCADE)
    profile = models.CharField(max_length = 200)
    description = models.TextField()
    location = models.CharField(max_length = 100)

    def get_absolute_url(self):
        return (str(self.id))

class Application(models.Model):
    student = models.ForeignKey(Profile, on_delete = models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete = models.CASCADE)