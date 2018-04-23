from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register_choice, name='register_choice'),
    url(r'^register/student$', views.UserFormView.as_view(), name = 'register_student'),
    url(r'^register/company$', views.UserFormView2.as_view(), name = 'register_company'),

    url(r'^login/$', views.login_x, name = 'login_x'),
    url(r'^login_auth$', views.login_button, name='login_auth'),
    url(r'^logout/$', views.logout_button, name = 'logout_button'),

    url(r'^user/$', views.user, name='user'),
    url(r'^user/(?P<u_id>[0-9]+)$', views.user_detail, name='user_detail'),
    url(r'^applications/$', views.applications, name="applications"),
    url(r'^user/add_work', views.add_work, name='add_work'),
    url(r'^add_work_button', views.add_work_button, name='add_work_button'),
    url(r'^user/add_education', views.add_education, name='add_education'),
    url(r'^add_education_button', views.add_education_button, name='add_education_button'),

    url(r'^internships/$', views.internships, name = 'internships'),
    url(r'^internships/add$', views.internship_add, name = 'internship_add'),
    url(r'^internships/add/add', views.internship_add_button, name = 'internship_add_button'),
    url(r'^posted', views.posted, name='posted'),
    url(r'^internships/(?P<internship_id>[0-9]+)/applications', views.intern_applications, name="intern_applications"),
    url(r'^internships/(?P<internship_id>[0-9]+)/delete', views.intern_delete, name="intern_delete"),

    url(r'internships/(?P<internship_id>[0-9]+)/$', views.intern_detail, name= 'intern_detail'),
    url(r'internships/(?P<internship_id>[0-9]+)/apply', views.apply, name= 'apply'),

]
