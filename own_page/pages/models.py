from django.db import models

# Create your models here.

class History(models.Model):
    Search = models.CharField(max_length=255)
    Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Search