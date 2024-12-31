from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import userForm

# Create your views here.
# def index(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("login"))
    
#     return render(request, "users/user.html")
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('bloghome'))
        else:
            return render(request, 'users/login.html', {
                "message": "Invalid Credentials."
            })
        
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
        "message":"Logged Out Successfully."
    })

def register(request):
    form = userForm()
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/login.html")
        else:
            print(form.errors)
            return redirect('register')
        
    return render(request, 'users/register.html',{
        'form': form
    })