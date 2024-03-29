from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

User = get_user_model()
class LoginForm(forms.Form):
    email= forms.CharField(
        widget= forms.TextInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )
    password= forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )

## Candidate Sign Up

class CandidateSignUpForm(UserCreationForm):
    email= forms.CharField(
        widget= forms.EmailInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )
    password1= forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )
    password2= forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )  
    class Meta():
        model = User
        fields = ['username','email', 'password1', 'password2', 'is_candidate']

        widget = {
            'username': forms.HiddenInput(),
            'is_candidate': forms.HiddenInput(),
        } 
        labels = {
            'username': '',
            'is_candidate': '',
        }
        required ={
            'is_candidate': True,
        }

    def clean_username(self):
        return 'default'
        return username     
    def __init__(self, *args, **kwargs):
        super(CandidateSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['username'].widget = forms.HiddenInput()
         
        

    ## Company Signup    
class CompanySignUpForm(UserCreationForm):
    email= forms.CharField(
        widget= forms.EmailInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )
    password1= forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )
    password2= forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )  
    class Meta():
        model = User
        fields = ['username','email', 'password1', 'password2']
          
    def clean_username(self):
        return 'default'
        return username     
    def __init__(self, *args, **kwargs):
        super(CompanySignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].required = False 
        ## User type Configuration
        # self.fields['is_admin'].initial = False
        # self.fields['is_candidate'].initial = False
        # self.fields['is_company'].initial = True
        # self.fields['is_contractor'].initial = False       

## Contractor Signup

class ContractorSignUpForm(UserCreationForm):
    email= forms.CharField(
        widget= forms.EmailInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )
    password1= forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )
    password2= forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )  
    class Meta():
        model = User
        fields = ['username','email', 'password1', 'password2']
          
    def clean_username(self):
        return 'default'
        return username     
    def __init__(self, *args, **kwargs):
        super(ContractorSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].required = False 
        ## User type Configuration
        self.fields['is_admin'].initial = False
        self.fields['is_candidate'].initial = False
        self.fields['is_company'].initial = False
        self.fields['is_contractor'].initial = True   

## Admin Signup

class AdminSignUpForm(UserCreationForm):
    email= forms.CharField(
        widget= forms.EmailInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )
    password1= forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )
    password2= forms.CharField(
        widget= forms.PasswordInput(
            attrs= {
                "class" : "form-control",
            }
        )

    )  
    class Meta():
        model = User
        fields = ['username','email', 'password1', 'password2']
          
    def clean_username(self):
        return 'default'
        return username     
    def __init__(self, *args, **kwargs):
        super(AdminSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].required = False 
        ## User type Configuration
        self.fields['is_admin'].initial = True
        self.fields['is_candidate'].initial = False
        self.fields['is_company'].initial = False
        self.fields['is_contractor'].initial = False                                   