from django.db import models
from django.contrib.auth.models import User

class Profile(User):
    is_student = models.BooleanField(default = False)
    is_company = models.BooleanField(default = False)

class Student(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)

class Company(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)

# Related to Student
class Education(models.Model):
    student = models.ForeignKey(Profile, on_delete = models.CASCADE)
    college = models.CharField(max_length=200)
    gpa = models.IntegerField()
    tenure_start = models.DateField(auto_now = False, auto_now_add = False)
    tenure_end = models.DateField(auto_now = False, auto_now_add = False)
    degree = models.CharField(max_length = 255)

class WorkEx(models.Model):
    student = models.ForeignKey(Profile, on_delete = models.CASCADE)
    company = models.CharField(max_length=200)  
    tenure_start = models.DateField(auto_now = False, auto_now_add = False)
    tenure_end = models.DateField(auto_now = False, auto_now_add = False)
    description = models.TextField()

class Achievement(models.Model):
    student = models.ForeignKey(Profile, on_delete = models.CASCADE)
    achievement = models.TextField()

# Related to company
class Internship(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    profile = models.CharField(max_length = 200)
    description = models.TextField()
    location = models.CharField(max_length = 100)

    def get_absolute_url(self):
        return (str(self.id))

class Application(models.Model):
    student = models.ForeignKey(Profile, on_delete = models.CASCADE)
    internship = models.ForeignKey(Internship, on_delete = models.CASCADE)