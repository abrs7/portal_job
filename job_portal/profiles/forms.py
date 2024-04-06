from django import forms

from .models import CompanyProfile, ContractorProfile
# from django.forms import ModelForm

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['name','established_date', 'address', 'logo', 'company_email','license_image' ,'company_website', 'company_detail','slug' ]
        widgets = {
            'slug': forms.HiddenInput(),
            'logo': forms.FileInput(attrs={'accept': 'image/*'}),
            'license_image': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        # widgets = {
        
        # }


class ContractorProfileForm(forms.ModelForm):
    class Meta:
        model = ContractorProfile
        fields = ['first_name', 'last_name', 'profile_pic', 'address', 'personal_email']
        
        widgets = {
            'slug': forms.HiddenInput(),
            
            'profile_pic': forms.FileInput(attrs={'accept': 'image/*'}),
        }
  
    