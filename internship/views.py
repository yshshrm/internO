from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import *

def index(request):
    return render(request, 'internship/index.html')

def login(request):
    return HttpResponse('This is the login page, sign in as student or company')

def student_login(request):
    return HttpResponse('<h1>Hi, student login</h1>')

def company_login(request):
    return HttpResponse('<h1>Hi, company login</h1>')

def logout(request):
    pass

class InternshipCreate(CreateView):
    model = Internship
    fields = ['profile', 'description', 'location']

def internships(request):
    # interns = Internship.objects.all()[page_num * 10 - 10 : page_num * 10]
    interns = Internship.objects.all()

    return render(request, 'internship/internships.html', {'interns' : interns})
    

def intern_detail(request, internship_id):
    # try:
    #     x = Internship.objects.get(id = internship_id)
    # except Internship.DoesNotExist:
    #     raise Http404("Album Does Not Exist")
    intern = get_object_or_404(Internship, id = internship_id)
    
    return render(request, 'internship/intern_detail.html', { 'intern' : intern })

def apply(request, internship_id):
    # intern = get_object_or_404(Internship, id = intern_id)
    return redirect('internships')