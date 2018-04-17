from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^register/student', views.student_register, name = 'student_register'),
    # url(r'^register/company', views.company_register, name = 'company_register'),
    url(r'^login/$', views.login, name = 'login'),
    url(r'^login/student/', views.student_login, name = 'student_login'),
    url(r'^login/company/', views.company_login, name = 'company_login'),

    url(r'^internships/add', views.InternshipCreate.as_view(), name = 'internship_add'),
    url(r'^internships/$', views.internships, name = 'internships'),
    url(r'internships/(?P<internship_id>[0-9]+)/$', views.intern_detail, name= 'intern_detail'),
    url(r'internships/(?P<internship_id>[0-9]+)/apply', views.apply, name= 'apply'),
]
