from django.shortcuts import render
from django.http import HttpResponse

from .models import *

company_logged_in = False
company_id = -1

student_logged_in = False
student_id = -1

def index(request):
    return HttpResponse('<h1>Hi</h1>')
    if(company_logged_in):
        render(request, )
    elif(student_logged_in):
        render(request, )
    else:
        render(request, )

def student_login(request):
    return HttpResponse('<h1>Hi, student login</h1>')

def company_login(request):
    return HttpResponse('<h1>Hi, company login</h1>')

def logout(request):
    company_logged_in = False
    company_id = -1
    student_logged_in = False
    student_id = -1

    return render(request, index.html)

def internships(request):
    if(company_logged_in):
        return HttpResponse('can\'t access since you are a company')

    elif(student_logged_in):
        return HttpResponse('Here are your internships')
    # internships = Internship.objects.all()[page_num * 10 - 10 : page_num * 10]
    
    else:
        return HttpResponse('Please log in')

