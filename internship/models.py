from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 255)
    phone = models.IntegerField()
    city = models.CharField(max_length = 200)
    is_student = models.BooleanField(default = False)
    is_company = models.BooleanField(default = False)

# Related to Student
class Education(models.Model):
    student_id = models.ForeignKey(Profile, on_delete = models.CASCADE)
    college = models.CharField(max_length=200)
    gpa = models.IntegerField()
    tenure_start = models.DateField(auto_now = False, auto_now_add = False)
    tenure_end = models.DateField(auto_now = False, auto_now_add = False)
    degree = models.CharField(max_length = 255)

class WorkEx(models.Model):
    student_id = models.ForeignKey(Profile, on_delete = models.CASCADE)
    company = models.CharField(max_length=200)  
    tenure_start = models.DateField(auto_now = False, auto_now_add = False)
    tenure_end = models.DateField(auto_now = False, auto_now_add = False)
    description = models.TextField()

class Achievement(models.Model):
    student_id = models.ForeignKey(Profile, on_delete = models.CASCADE)
    achievement = models.TextField()

# class Company(models.Model):
#     email = models.EmailField(max_length = 250)
#     name = models.CharField(max_length = 200)
#     phone = models.IntegerField()
#     description = models.TextField()

# Related to company
class Internship(models.Model):
    # company_id = models.ForeignKey(Profile, on_delete = models.CASCADE)
    profile = models.CharField(max_length = 200)
    description = models.TextField()
    location = models.CharField(max_length = 100)

    def get_absolute_url(self):
        return (str(self.id))

class Application(models.Model):
    student_id = models.ForeignKey(Profile, on_delete = models.CASCADE)
    internship_id = models.ForeignKey(Internship, on_delete = models.CASCADE)