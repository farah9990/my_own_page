
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Home.html', views.Home, name='Home'),
    path('About.html', views.About, name='About'),
    path('Contact.html', views.Contact, name='Contact'),
    path('Courses.html', views.Courses, name='Courses'),
    path('Wep-application​s.html', views.WepApplications, name='Wep-applications'),
    path('Skills.html', views.Skills, name='Skills'),
    path('Phone-application​s.html', views.PhoneApplications, name='Phone-applications'),

]
