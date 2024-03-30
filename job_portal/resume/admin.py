# admin.py

from django.contrib import admin
from .models import Resume, Education, Experience

# Register your models here
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Experience)
