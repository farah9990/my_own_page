from django.contrib import admin
from .models import History, Person, Event

# Register your models here.
admin.site.register(History)
admin.site.register(Person)
admin.site.register(Event)