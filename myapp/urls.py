from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='my_home'),
    path('', views.about, name='my_about'),
    path('', views.contact, name='my_contact'),
    path('', views.services, name='my_services'),
    path('', views.servicesdetails, name='my_servicedetails'),
    path('', views.blog, name='my_blog'),
    path('', views.blogdetails, name='blogdetails'),
    path('', views.projects, name='my_projects'),
    path('', views.projectsdetails, name='my_projectsdetails'),
    path('', views.sampleinnerpage, name='sampleinnerpage'),

]
