from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_year', 'genre', 'available_copies']
    list_filter = ['genre', 'published_year']
    search_fields = ['title', 'author']