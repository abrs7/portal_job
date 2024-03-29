from django import forms
from .models import Resume, Education, Experience


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['first_name', 'last_name', 'birth_date', 'occupation', 'bio', 'profile_picture', 'cv']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_date', 'end_date']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company','job_description', 'start_date', 'end_date']   
   
       