from django import forms
from .models import JobPost, ContractPost

class JobPostForm(forms.ModelForm):
   class Meta:
    model = JobPost
    fields = '__all__'
    exclude = ['slug']
    widgets = {
        'slug': forms.HiddenInput(),
    }

    

class ContractorPostForm(forms.ModelForm):
    class Meta:
       model = ContractPost
       fields = '__all__'
       exclude = ['slug']

       widgets = {
        'slug': forms.HiddenInput(),
        }

       
    
