from django.contrib import admin

# Register your models here.
from .models import *


class BooksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author')
    


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'year_of_birth')
    


admin.site.register(Books, BooksAdmin)
admin.site.register(Author, AuthorAdmin)