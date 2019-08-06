from django.contrib import admin

# Register your models here.
from .models import Snippet

admin.site.register(Snippet,admin.ModelAdmin)