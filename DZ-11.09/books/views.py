from django.shortcuts import render
from .models import Books


def main_page(request):
    return render(request, 'index.html')


def all_books(request):
    books = {
        'books': Books.objects.all()
    }
    return render(request, 'books.html', books)
