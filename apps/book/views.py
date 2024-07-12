from django.shortcuts import render
from . import models
from django.http import HttpResponse

# Create your views here.

def book_detail(request,isbn):

    book = models.Book.objects.get(pk=isbn)

    response = f"""
        <html>
            <h1>{book.title}</h1>
            <p><b>isbn</b>: {book.isbn}</p>
            <p><b>description</b>: {book.description}</p>
            <p><b>Pages</b>: {book.page_count}</p>
            <p><b>Published Year</b>: {book.published_date}</p>
            <p><b>Publisher</b>: {book.publisher}</p>
            <p><b>Language</b>: {book.lang}</p>
            <p><b>Edition</b>: {book.edition}</p>
            <p><b>Format</b>: {book.book_format}</p>

        </html>
        """

    return HttpResponse(response)      


    
