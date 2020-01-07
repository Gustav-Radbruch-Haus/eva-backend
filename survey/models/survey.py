from django.db import models

# Create your models here.
class Survey(models.Model):
    name = models.CharField()
    dateOfCreation = models.DateTimeField(auto_now_add=True)
    