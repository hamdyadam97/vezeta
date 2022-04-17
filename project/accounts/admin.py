from django.contrib import admin

# Register your models here.
from .models import Profile, Clinic

admin.site.register(Profile)
admin.site.register(Clinic)