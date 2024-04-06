from django.shortcuts import render, redirect
from .forms import CandidateSignUpForm, LoginForm, CompanySignUpForm, ContractorSignUpForm, AdminSignUpForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from profiles.models import CompanyProfile, ContractorProfile

# Create your views here
def index(request):
    return render(request,'index.html')

from django.db import IntegrityError

def candidate_register(request):
    if request.method == 'POST':
        form = CandidateSignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Account is already taken. Please choose a different one.')
                return redirect('index')
            
            else:
                # Set a default username (e.g., based on the email)
                username = email.split('@')[0]  # Use the part before the '@' symbol as the username
                # Create the user with the default username
                try:
                    user = form.save(commit=False)
                    user.username = username
                    user.save()
                    messages.success(request, 'User created successfully. You can now log in.')
                    return redirect('login')
                except IntegrityError:
                    messages.error(request, 'An error occurred while saving the user. Please try again.')
                    return render(request, 'candidate_register.html', {'form': form})
    else:
        form = CandidateSignUpForm()
    return render(request, 'candidate_register.html', {'form': form})

## Company View
def company_register(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Account is already taken. Please choose a different one.')
                return redirect('index')
            
            else:
                # Set a default username (e.g., based on the email)
                username = email.split('@')[0]  # Use the part before the '@' symbol as the username
                # Create the user with the default username
                try:
                    user = form.save(commit=False)
                    user.username = username
                    user.save()
                    messages.success(request, 'User created successfully. You can now log in.')
                    return redirect('login')
                except IntegrityError:
                    messages.error(request, 'An error occurred while saving the user. Please try again.')
                    return render(request, 'company_register.html', {'form': form})
    else:
        form = CompanySignUpForm()
    return render(request, 'company_register.html', {'form': form})
##Contractor Signup

def contractor_register(request):
    if request.method == 'POST':
        form = ContractorSignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Account is already taken. Please choose a different one.')
                return redirect('index')
            
            else:
                # Set a default username (e.g., based on the email)
                username = email.split('@')[0]  # Use the part before the '@' symbol as the username
                # Create the user with the default username
                try:
                    user = form.save(commit=False)
                    user.username = username
                    user.save()
                    messages.success(request, 'User created successfully. You can now log in.')
                    return redirect('login')
                except IntegrityError:
                    messages.error(request, 'An error occurred while saving the user. Please try again.')
                    return render(request, 'contractor_register.html', {'form': form})
    else:
        form = ContractorSignUpForm()
    return render(request, 'contractor_register.html', {'form': form})

def login(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)  # Set the user in the session
                if user.is_candidate:
                    return redirect('home_candidate')
                if user.is_company:
                    return redirect('home_company')
                if user.is_contractor:
                    return redirect('home_contractor')
            else:
                msg = 'Invalid Credentials'
                messages.error(request, msg)

    return render(request, 'login.html', {'form': form})
def LogOutView(request):
    logout(request)
    return redirect('index')
@login_required
def home_candidate(request):
    user = request.user
    return render(request, 'home_candidate.html',{'user':request.user})  

@login_required          
def home_company(request):
   
    user = request.user
    company_profile = get_object_or_404(CompanyProfile, user_id = user.id)

    return render(request, 'home_company.html',{'company_profile':company_profile})

@login_required
def home_contractor(request):
    user = request.user
    contractor_profile = get_object_or_404(ContractorProfile, user_id = user.id)
    return render(request, 'home_contractor.html', {'contractor_profile': contractor_profile})
                  
def index(request):
   
    return render(request, 'index_copy.html')         
        




    