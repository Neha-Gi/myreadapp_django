from django.shortcuts import render
from .models import Book

# Create your views here.
def book_detail(request, isbn):
    book = Book.objects.get(pk=isbn)
    context = {
        "book": book,
        "tags": ', '.join(str(tag) for tag in book.tag.all()),
        "authors": ', '.join(str(author) for author in book.authors.all())
    }

    return render(request, "book_detail.html", context)
