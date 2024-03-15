from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {'name':'Home'})

def Home(request):
    return render(request, 'pages/Home.html', {'name':'Home'})

def About(request):
    return render(request, 'pages/About.html',  {'name':'About'})

def Contact(request):
    return render(request, 'pages/Contact.html', {'name':'Contact'})

def Skills(request):
    return render(request, 'pages/Skills.html', {'name':'Skills'})

def Courses(request):
    return render(request, 'pages/Courses.html', {'name':'Courses'})

def WepApplications(request):
    return render(request, 'pages/WepApplication.html', {'name':'Wep-applications'})

def PhoneApplications(request):
    return render(request, 'pages/PhoneApplication.html', {'name':'Phone-applications'})

def Other(request):
    return render(request, 'pages/Other.html', {'name':'Other'})

