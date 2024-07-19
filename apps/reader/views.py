from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from .models import Reader

# Create your views here.
def login_view(request):
    
    # pre-submit state
    error_message = None
    form = AuthenticationForm()

    # post-submit state
    if request.method == "POST":
        form = AuthenticationForm(data =request.POST)

        # Validate the form
        if form.is_valid():
            # Extract username and password
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # Authenticate the user
            reader:Reader | None = authenticate(
                username = username,
                password = password
            )
            #breakpoint()
            if reader is not None:
                login(request,reader)
                return redirect('reader-urls:reader-profile')
        error_message = 'Sorry Try again'
    context = {'form':form,'error_message':error_message}  
    return render(request,'login.html',context) 
@login_required
def profile(request):
   # breakpoint()
 
    return render(request,'profile.html')

def logout_view(request):
    if request.method == 'GET':
        return render(request, 'logout.html') 
    elif request.method == 'POST':
        logout(request)
        return redirect('reader-urls:reader-login')