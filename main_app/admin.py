from django.contrib import admin
from .models import Sunset, Viewing, Experience

# Register your models here.
admin.site.register(Sunset)

admin.site.register(Viewing)

admin.site.register(Experience)