from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to display
    search_fields = ('title', 'author')                     # searchable fields
    list_filter = ('publication_year',)                     # filters by publication year

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)
