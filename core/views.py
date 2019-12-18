from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from core.models import *

# Create your views here.
def splash(request):
    return render(request, 'splash.html', {'username': request.user.username})

def login_page(request):
    return render(request, 'login.html', {})

def home(request):
    tweets = Tweet.objects.all().order_by("date")
    return render(request, 'home.html', {'tweets': tweets})

# render user profile
def profile(request):
    tweets = Tweet.objects.filter(users=request.user)
    return render(request, 'profile.html', {'tweets': tweets})

def hashTag(request):
    return render(request, 'hash.html', {})

# authorize log in
def loginauth(request):
    if request.method == "POST":

        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])

        # check to make sure user exists
        if user is not None:
            login(request, user)
            print("Log in success")
            return redirect('/home')

    print("User does not exist")
    return redirect('/login')