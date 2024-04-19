from django.db import models
from datetime import date

# Create your models here.

class History(models.Model):
    Search = models.CharField(max_length=255)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Search

class Person(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    bio = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event_date = models.DateField()
    event_description = models.TextField()

    def __str__(self):
        return f"{self.person.name}'s {self.event_description[:20]}..."