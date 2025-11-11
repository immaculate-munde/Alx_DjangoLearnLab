from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book    
from django.http import HttpResponse


# Create your views here.
def home(request):
    """Simple home page redirecting to the list of books."""
    return HttpResponse("Welcome to the Library Project! Visit /books/ to see all books.")

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view: show details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
