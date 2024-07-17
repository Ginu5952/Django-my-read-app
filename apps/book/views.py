from django.shortcuts import render
from . import models
from django.http import HttpResponse
import ipdb
from .forms import PostBookForm

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

        # validation
        if form.is_valid():
            # TODO:save to database
            # TODO:redirect to home page
            pass



