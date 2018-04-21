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

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse('wrong')

def logout_view(request):
    logout(request)
    return redirect( '/')

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
    # intern = get_object_or_404(Internship, id = intern_id)
    return redirect('internships')

class UserFormView(View):
    form_class = UserForm
    template_name = "internship/register.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
        
        return render(request, self.template_name, {'form' : form})

class LoginFormView(View):
    form_class = LoginForm
    template_name = "internship/login.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(user)
            return render(request, 'index')
        else:
            return render(request, self.template_name, {'form' : form})

        

        # if form.is_valid():
        #     user = form.save(commit = False)
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']

        #     user.set_password(password)
        #     # user.save()

        #     user = authenticate(username=username, password=password)

        #     if user is not None:
        #         if user.is_active:
        #             login(request, user)
        #             return redirect('index')
        
        

