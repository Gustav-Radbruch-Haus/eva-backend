from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Rental)
admin.site.register(models.RentalComment)
admin.site.register(models.Facility)