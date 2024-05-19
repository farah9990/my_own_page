from django.shortcuts import render, redirect
from django.db.models import Q, Avg, Min
from django.db.models.functions import Extract
from .models import History, Person, Event
from datetime import datetime , date
from django.shortcuts import redirect, get_object_or_404
from .forms import SearchForm

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
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['q']
            if query:
                History.objects.create(Search=query, Date=datetime.now())
                return redirect(f'https://www.google.com/search?q={query}')
    else:
        form = SearchForm()
    
    # Filter people born after '1975-01-01'
    people = Person.objects.filter(birth_date__gt='1975-01-01')
    # Exclude people named 'John Doe'
    people_exclude = people.exclude(name='John Doe')
    # Limit to first 2 people
    limited_people = people[:2]
    # Combine Q operators using & and |
    query = Q(name='John Doe') & (Q(birth_date__gt='1975-01-01') | Q(bio__icontains='engineer'))
    people_filtered = Person.objects.filter(query)
    # Order people by birth date in descending order
    ordered_people = Person.objects.order_by('-birth_date')
    # Count of people born after '1975-01-01'
    count_people = Person.objects.filter(birth_date__gt='1975-01-01').count()
    # Calculate age and annotate it to the queryset
    people_with_age = Person.objects.all().annotate(
        age=date.today().year - Extract('birth_date', 'year')
    )
    # Calculate average age
    avg_age = people_with_age.aggregate(avg_age=Avg('age'))
    # Find the minimum event date for each person
    min_event_dates = Event.objects.values('person__name').annotate(min_date=Min('event_date')).order_by()
    
    # Fetch all history items for the datalist
    history_items = History.objects.all()

    return render(request, 'pages/Other.html', {
        'name': 'Other',
        'form': form,
        'limited_people': limited_people,
        'people_filtered': people_filtered,
        'people_exclude': people_exclude,
        'ordered_people': ordered_people,
        'count_people': count_people,
        'avg_age': avg_age['avg_age'] if avg_age['avg_age'] else 0,
        'min_event_dates': min_event_dates,
        'history_items': history_items,
    })
    
def history_view(request):
    history_items = History.objects.all()  # Query all History objects
    return render(request, 'pages/History.html', {'name': 'History', 'History': history_items})

def delete_history(request, pk):
    history_item = get_object_or_404(History, pk=pk)
    if request.method == 'POST':
        history_item.delete()
        return redirect('history_view')
    return redirect('history_view')