from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
# Create your views here
def index(request):
    return render(request,'index.html')

from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken. Please choose a different one.')
                return render(request, 'register.html', {'form': form})
            # If username is unique, save the form
            try:
                user = form.save()
                messages.success(request, 'User created successfully. You can now log in.')
                return redirect('login')
            except IntegrityError:
                messages.error(request, 'An error occurred while saving the user. Please try again.')
                return render(request, 'register.html', {'form': form})
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})


# def company_signup(request):
#     msg = None
#     if request.method == 'POST':
#         form =         

def login(request):
    form = LoginForm(request.POST or None)
    # msg = None 

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                # if user.is_candidate:
                #     return redirect('home')
                # login(request, user)
                messages.success(request,'Successfully loged in!')
                return redirect('home_candidate')
            else:
                msg = 'Invalid Credentials'
                messages.error(request, msg) 
    return render(request, 'login.html', {'form': form})        

def home_candidate(request):
    user = request.user
    return render(request, 'home_candidate.html',{'user':user})            
def home(request):
   
    return render(request, 'home.html')                  
def index(request):
   
    return render(request, 'index_copy.html')         
        




    