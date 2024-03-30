# forms.py

from django import forms
from .models import Resume, Education, Experience

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['first_name', 'last_name', 'birth_date', 'occupation', 'bio', 'profile_picture', 'cv']

    def save_resume(self, user):
        resume = self.save(commit=False)
        resume.user = user
        resume.save()
        return resume

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'start_date', 'end_date']

    def save_education(self, resume):
        education = self.save(commit=False)
        education.resume = resume
        education.save()
        return education

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company','job_description', 'start_date', 'end_date']  

    def save_experience(self, resume):
        experience = self.save(commit=False)
        experience.resume = resume
        experience.save()
        return experience
