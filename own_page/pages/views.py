from django.shortcuts import render, redirect
from .models import History
from datetime import datetime
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
    if request.method == 'POST':
        query = request.POST.get('q', '')
        
        if query:
            History.objects.create(Search=query, Date=datetime.now())

            # Redirect to Google for search
            return redirect(f'https://www.google.com/search?q={query}')

    return render(request, 'pages/Other.html', {'name': 'Other', 'History': History.objects.all()})

