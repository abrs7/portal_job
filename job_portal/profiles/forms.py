from django import forms
from .models import CompanyProfile, ContractorProfile
# from django.forms import ModelForm

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['name','logo','established_date', 'address', 'license_image', 'company_email', 'company_website', 'company_detail' ]



class ContractorProfileForm(forms.ModelForm):

    class Meta:
        model = ContractorProfile
        fields = ['first_name', 'last_name', 'profile_pic', 'address', 'personal_email']
