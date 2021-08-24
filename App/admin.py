from django.contrib import admin
from .models import UserProfile
from . import signals

# Register your models here.

admin.site.register(UserProfile)
