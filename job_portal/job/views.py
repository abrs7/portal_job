from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPost, ContractPost
from .forms import JobPostForm, ContractorPostForm
from profiles.models import CompanyProfile, ContractorProfile

from accounts.models import User 

def create_job(request):
    if not request.user.is_authenticated or not request.user.is_company:
        return redirect('logout')
    
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            company_profile = CompanyProfile.objects.get(user = request.user)
            job_post = form.save(commit=False)
            job_post.poster = company_profile
            job_post.save()
            return redirect('job_list')
        else:
            print(form.errors)
    else:
        form = JobPostForm()        
    
    return render(request, 'job/company_post.html', {'form': form})

def create_contract(request):
    if not request.user.is_authenticated or not request.user.is_contractor:
        return redirect('logout')
    
    if request.method == 'POST':
        form = ContractorPostForm(request.POST)
        if form.is_valid():
            contractor_profile = ContractorProfile.objects.get(user = request.user)
            contract_post = form.save(commit=False)
            contract_post.poster = contractor_profile
            contract_post.save()
            return redirect('contract_list')
        else:
            print(form.errors)
    else:
        form = ContractorPostForm()        
    
    return render(request, 'job/contract_post.html', {'form': form})

def show_jobs(request):
    company_profile = get_object_or_404(CompanyProfile, user = request.user)
    jobs = JobPost.objects.filter(poster = company_profile)

    return render(request, 'job/company_job.html', {'jobs': jobs})

def show_contracts(request):
    contractor_profile = get_object_or_404(ContractorProfile, user = request.user)
    contracts = ContractPost.objects.filter(poster = contractor_profile)

    return render(request, 'job/contractor_job.html', {'contracts': contracts})