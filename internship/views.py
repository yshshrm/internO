from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy 
from django.views import generic
from django.views.generic import View

from .models import *
from .forms import *

def index(request):
    return render(request, 'internship/index.html')

def login_x(request):
    return render(request, 'internship/login.html')

def login_button(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'internship/login.html')

def logout_button(request):
    logout(request)
    return redirect( '/')

def register_choice(request):
    return render(request, 'internship/register.html')

def internship_add(request):
    return render(request, 'internship/internship_form.html')

def internship_add_button(request):
    profile = request.POST['profile']
    description = request.POST['description']
    location = request.POST['location']
    user_id = request.user.id
    p = Profile.objects.get(id = user_id)
    i = Internship(company = p, description = description, location = location, profile = profile)
    i.save()
    return redirect('/')

class InternshipCreate(CreateView):
    model = Internship
    fields = ['profile', 'description', 'location']

class InternshipUpdate(UpdateView):
    model = Internship
    fields = ['profile', 'description', 'location']

class InternshipDelete(DeleteView):
    model = Internship
    success_url = reverse_lazy('index')

def internships(request):
    # interns = Internship.objects.all()[page_num * 10 - 10 : page_num * 10]
    interns = Internship.objects.all()
    return render(request, 'internship/internships.html', {'interns' : interns})
    
def intern_detail(request, internship_id):    
    intern = get_object_or_404(Internship, id = internship_id)
    return render(request, 'internship/intern_detail.html', { 'intern' : intern })

def apply(request, internship_id):
    i = Internship.objects.get(id = internship_id)
    application = Application(student = request.user.profile, internship = i)
    application.save()
    return redirect('internships')

def applications(request):
    a = {}
    if request.user.is_authenticated and request.user.profile.is_student:
        a = Application.objects.filter(student = request.user.profile)
    return render(request, 'internship/applications.html', { 'applications' : a })

def posted(request):
    a = {}
    if request.user.is_authenticated and request.user.profile.is_company:
        a = Internship.objects.filter(company = request.user.profile)
    return render(request, 'internship/posted.html', {'interns' : a})

def intern_applications(request, internship_id):
    a = {}
    if request.user.is_authenticated and request.user.profile.is_company:
        i = Internship.objects.filter(id = internship_id)
        a = Application.objects.filter(internship = i)
    return render(request, 'internship/intern_applications.html', {'applications' : a})

def intern_delete(request, internship_id):
    instance = Internship.objects.get(id=internship_id)
    instance.delete()
    return redirect('/')

def user(request):
    u = Profile.objects.get(id = request.user.profile.id)
    e = Education.objects.filter(student = u)
    w = WorkEx.objects.filter(student = u)
    return render(request, 'user/my_details.html', {'profile' : u, 'education': e, 'work': w})

def user_detail(request, u_id):
    u = Profile.objects.get(id = u_id)
    e = Education.objects.filter(student = u)
    w = WorkEx.objects.filter(student = u)
    return render(request, 'user/detail.html', {'profile' : u, 'education': e, 'work': w})

class UserFormView(View):
    form_class = UserForm
    template_name = "internship/register_student.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            user.set_password(password)
            user.is_student = True
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                    
        
        return render(request, self.template_name, {'form' : form})

class UserFormView2(View):
    form_class = UserForm
    template_name = "internship/register_company.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            user.set_password(password)
            user.is_company = True
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
        
        return render(request, self.template_name, {'form' : form})       

def add_work(request):
    return render(request, 'user/add_work.html')

def add_work_button(request):
    c = request.POST['company']
    d = request.POST['description']
    p = request.user.profile
    w = WorkEx(company = c, description = d, student = p)
    w.save()
    return redirect('/user')

def add_education(request):
    return render(request, 'user/add_education.html')

def add_education_button(request):
    c = request.POST['college']
    d = request.POST['degree']
    g = request.POST['gpa']
    p = request.user.profile
    e = Education(college = c, degree = d, gpa = g, student = p)
    e.save()
    return redirect('/user')
