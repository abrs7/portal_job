from django.shortcuts import render, redirect
from .forms import CompanyProfileForm, ContractorProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model 
from django.views.generic import UpdateView
from django.shortcuts import get_object_or_404
from .models import CompanyProfile, ContractorProfile
from accounts.models import User

@login_required
def company_profile(request):
    user = request.user
    company_user = get_object_or_404(User, id=user.id, is_company=True)
    company = get_object_or_404(CompanyProfile, user_id = user.id)
   
    if not company_user:
        return redirect('edit_profile')

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, request.FILES)
        

        if form.is_valid():
            if CompanyProfile.objects.filter(user=company_user).exists():
                messages.warning(request, 'User profile already exists')
                return redirect(reverse('edit_profile', kwargs={'slug': company.slug}))  # Provide the slug value here

            company_profile = form.save(commit=False)
            company_profile.user = user
            company_profile.save()
            messages.success(request, 'You have successfully added your profile!')
            return redirect('show_company')
        else:
            messages.warning(request, 'Invalid form submission. Please correct the errors.')
    else:
        form = CompanyProfileForm()

    return render(request, 'profile/company_profile.html', {'form': form})


def contractor_profile(request):
    user = request.user
    contractor_user = get_object_or_404(User, id=user.id, is_contractor=True)
    contractor = get_object_or_404(ContractorProfile, user_id = user.id)
   
    if not contractor_user:
        return redirect('home')
    

    if request.method == 'POST':
        form = ContractorProfileForm(request.POST, request.FILES)
        

        if form.is_valid():
            if ContractorProfile.objects.filter(user=contractor_user).exists():
                messages.warning(request, 'User profile already exists')
                return redirect(reverse('contractor_edit', kwargs={'slug': contractor.slug}))  # Provide the slug value here

            contractor_profile = form.save(commit=False)
            contractor_profile.user = user
            contractor_profile.save()
            messages.success(request, 'You have successfully added your profile!')
            return redirect('show_contractor')
        else:
            messages.warning(request, 'Invalid form submission. Please correct the errors.')
    else:
        form = ContractorProfileForm()

    return render(request, 'profile/contractor_profile.html', {'form': form})
       



class Company_Update(UpdateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    # fields = ['__all__']
    template_name = 'profile/company_edit.html'

    def get_object(self, queryset=None):
        company = get_object_or_404(CompanyProfile, user=self.request.user, slug=self.kwargs['slug'])
        return company

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    success_url = '/profiles/show_company/{slug}/'


class Contractor_Update(UpdateView):
    model = ContractorProfile
    form_class = ContractorProfileForm
    # fields = ['__all__']
    template_name = 'profile/contract_edit.html'

    def get_object(self, queryset=None):
        contractor = get_object_or_404(ContractorProfile, user=self.request.user, slug=self.kwargs['slug'])
        return contractor

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    success_url = '/profiles/show_contractor/{slug}/'





def show_profile(request, user_slug):
    company_profile = get_object_or_404(CompanyProfile, slug = user_slug )
    return render(request, 'profile/show_company.html', {'company_profile': company_profile})


def show_contractor(request, user_slug):
    contractor_profile = get_object_or_404(ContractorProfile, slug = user_slug )
    return render(request, 'profile/show_contractor.html', {'contractor_profile': contractor_profile})