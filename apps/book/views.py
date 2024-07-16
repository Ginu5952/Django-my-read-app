from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.

def book_detail(request,isbn):

    book = models.Book.objects.get(pk=isbn)

    context = {
        "book": book,
        "tags": ', '.join(str(tag) for tag in book.tags.all()),
        "authors": ', '.join(str(author) for author in book.authors.all())
    }

   
    return render(request, 'book_detail.html',context)     


    
