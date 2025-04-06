from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import userForm

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            response = HttpResponseRedirect(reverse('bloghome'))
            response.set_cookie('username', user.username, max_age=3600) #Expires in 1hr
            return response
        else:
            return render(request, 'users/login.html', {
                "message": "Invalid Credentials."
            })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    # Optionally clear session data
    request.session.flush()
    # Prepare a response and delete the cookie
    response = render(request, "users/login.html", {
        "message": "Logged Out Successfully."
    })
    response.delete_cookie('username')
    return response

def register(request):
    form = userForm()
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            # You could set a session message or cookie here after successful registration
            return render(request, "users/login.html")
        else:
            print(form.errors)
            return redirect('register')
    return render(request, 'users/register.html', {
        'form': form
    })
