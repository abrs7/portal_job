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
class SignUpForm(UserCreationForm):
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
        fields = ['username','email', 'password1', 'password2', 'is_candidate', 'is_company', 'is_contractor', 'is_admin']
          
    def clean_username(self):
        return 'default'
        return username     
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['username'].required = False