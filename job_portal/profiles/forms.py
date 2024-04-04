from django import forms

from .models import CompanyProfile, ContractorProfile
# from django.forms import ModelForm

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['name','established_date', 'address', 'company_email', 'company_website', 'company_detail' ]

        # widgets = {
        #     'logo': forms.FileInput(attrs={'accept': 'image/*'}),
        #     'license_image': forms.FileInput(attrs={'accept': 'image/*'}),
        # }


class ContractorProfileForm(forms.ModelForm):

    class Meta:
        model = ContractorProfile
        fields = ['first_name', 'last_name', 'profile_pic', 'address', 'personal_email']
