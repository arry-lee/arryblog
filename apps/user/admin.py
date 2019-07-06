from django.contrib import admin
# Register your models here.
from user.models import User,Activity


admin.site.register(User,admin.ModelAdmin)
admin.site.register(Activity,admin.ModelAdmin)
