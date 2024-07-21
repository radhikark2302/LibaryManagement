from django.contrib import admin

# Register your models here.
# store/admin.py
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_borrowed')
    search_fields = ('title', 'author')
    list_filter = ('is_borrowed', 'published_date')
