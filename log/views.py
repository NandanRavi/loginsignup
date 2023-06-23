from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm

# Create your views here.

def home(request):
    return render(request, 'log/home.html')

def dashboard(request):
    return render(request, 'log/dashboard.html')

def userLogin(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":
        username = request.POST['Username'].lower()
        password = request.POST['Password']

        try:
            user = User.objects.get(username=username)
        except:
            pass
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect('dashboard')
        else:
            messages.error(request, "Username or Password is incorrect")

    return render(request, 'log/login-signup.html')

def userLogout(request):
    logout(request)
    messages.error(request, "User was Logged out")
    return redirect('login')

def userRegister(request):

    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registered")
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "An error is generated")
    else:
        form = CustomUserCreationForm()

    context = {'page':page, 'form':form}
    return render(request, 'log/login-signup.html', context)