from django.contrib import admin

# Register your models here.
from .models import Snippet,LeetCode

admin.site.register(Snippet,admin.ModelAdmin)
admin.site.register(LeetCode,admin.ModelAdmin)
