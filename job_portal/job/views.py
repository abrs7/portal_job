from django.shortcuts import render, redirect
from .models import JobPost, ContractPost
from .forms import JobPostForm, ContractorPostForm

from accounts.models import User 

def create_job(request):
    if not request.user.is_authenticated or not request.user.is_company:
        return redirect('logout')
    
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job_post = form.save(commit=False)
            job_post.poster = request.user.companyprofile
            job_post.save()
            return redirect('job_list')
    else:
        form = JobPostForm()
    
    return render(request, 'job/company_post.html', {'form': form})

def create_contract(request):
    if not request.user.is_authenticated or not request.user.is_contractor:
        return redirect('logout')
    
    if request.method == 'POST':
        form = ContractorPostForm(request.POST)
        if form.is_valid():
            contract_post = form.save(commit=False)
            contract_post.poster = request.user.contractorprofile
            contract_post.save()
            return redirect('job_list')
    else:
        form = ContractorPostForm()
    
    return render(request, 'job/contractor_post.html', {'form': form})
