from django.shortcuts import render, redirect
from .forms import CompanyProfileForm, ContractorProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model 
from django.shortcuts import get_object_or_404
from .models import CompanyProfile, ContractorProfile
from accounts.models import User

@login_required
def company_profile(request):
    user = request.user
    company_user = get_object_or_404(User, id=user.id, is_company=True)

    if not company_user:
        return redirect('edit_profile')

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES)
        

        if form.is_valid():
            if CompanyProfile.objects.filter(user=user).exists():
                messages.warning(request, 'User profile already exists')
                return redirect('edit_profile')

            company_profile = form.save(commit=False)
            company_profile.user = user
            company_profile.save()
            messages.success(request, 'You have successfully added your profile!')
            return redirect('job_post')
        else:
            messages.warning(request, 'Invalid form submission. Please correct the errors.')
    else:
        form = CompanyProfileForm()

    return render(request, 'profile/company_profile.html', {'form': form})


def contractor_profile(request):
    form = ContractorProfileForm()

    if request.method == 'POST':
        form = ContractorProfileForm(request.POST)
        if form.is_valid():
            if ContractorProfile.objects.filter(form=form).exists:
                return redirect('job_post')
            else: 
                ContractorProfileForm()

        else:
            return redirect('login')
    return render(request, 'profile/contractor_profile.html', {'form': form})

def job_creation(request):
    return render(request, 'profile/job_post.html')