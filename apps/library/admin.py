from __future__ import absolute_import

from django.contrib import admin

from .models import Book, Author

class BookAdmin(admin.ModelAdmin):
    list_display =('title', 'format_year_published')

    def format_year_published(self, obj):
        if not obj.year_published:
            return '?'
        return obj.year_published.strftime(u'%Y')
    format_year_published.short_description = 'Year published'
    format_year_published.admin_order_field = 'year_published'

admin.site.register(Book, BookAdmin)



class AuthorAdmin(admin.ModelAdmin):
    list_display =('name',)
admin.site.register(Author, AuthorAdmin)
