from django.shortcuts import render,redirect
from . import models
from django.http import HttpResponse
import ipdb
from .forms import PostBookForm
from apps.book.models import Book

# Create your views here.

def book_detail(request,isbn):

    book = models.Book.objects.get(pk=isbn)

    context = {
        "book": book,
        
    }
 
    return render(request, 'book_detail.html',context)     


#def book_post(request):
    #ipdb.set_trace()
  #  return render(request,'post.html')    

def book_post(request):
    # get our form in the 2 states
    # pre-submit - GET
    # post-submit - POST
   # ipdb.set_trace()
    if request.method == 'GET':
        form = PostBookForm()
        context = {"form":form}
        return render(
            request,
            'book_post.html',
            context 
        )
    elif request.method == 'POST':
        data = request.POST
        form = PostBookForm(data)

         # Validation
        if form.is_valid():
            data = form.cleaned_data
            # TODO: Save to database
            book = models.Book(
                isbn=data['isbn'],
                title=data['title'],
                page_count=data['pages'],
                description=data['description'],
                category=data['category'],
                published_date = data['published_year'],
                publisher=data['publisher'],
                lang=data['language'],
                edition=data['edition'],
                book_format=data['book_format']
            )
            # save book first, to avoid `ValueError: Cannot add *: instance is on database "default", value is on database "None"`
            book.save()

            book.tags.set(data['tags'])
            book.save()

            #  Redirect to home page using `app-name: url-name`
            return redirect('myread-urls:home-page')