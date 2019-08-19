from django.contrib import admin

# Register your models here.
from .models import Note,Group,Tag

admin.site.register(Note,admin.ModelAdmin)
admin.site.register(Group,admin.ModelAdmin)
admin.site.register(Tag,admin.ModelAdmin)