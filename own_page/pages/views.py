from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {'name':'farah'})

def Home(request):
    return render(request, 'pages/Home.html')

def About(request):
    return render(request, 'pages/About.html')

def Contact(request):
    return render(request, 'pages/Contact.html')

def Skills(request):
    return render(request, 'pages/Skills.html')

def Courses(request):
    return render(request, 'pages/Courses.html')

def WepApplications(request):
    return render(request, 'pages/Wep-applications.html')

def PhoneApplications(request):
    return render(request, 'pages/Phone-applications.html')