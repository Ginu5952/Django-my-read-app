from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Reader

# Create your views here.

def login_view(request):

    # pre-submit state
    error_message = None
    form = AuthenticationForm()

    # post-submit state
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        #validate the form
        if form.is_valid():
            # extract username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            reader: Reader | None = authenticate(
                username=username,
                password=password
            ) 
            if reader is not None:
                login(request, reader)
                return redirect('reader-urls:reader-profile')
            
        # set an error message
        error_message = 'Sorry, Something went wrong. Try again'    

    context = {'form':form, 'error_message':error_message}

    return render(request,'login.html',context)    


def profile(request):
    breakpoint()
    return render(request, 'profile.html')
