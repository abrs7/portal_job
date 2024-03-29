from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm, EducationForm, ExperienceForm

def create_resume(request):
    if request.method == 'POST': 
        resume_form = ResumeForm(request.POST, request.FILES)
        education_form = EducationForm(request.POST)
        experience_form = ExperienceForm(request.POST)

        if all([resume_form.is_valid(), education_form.is_valid(), experience_form.is_valid()]):
            resume = resume_form.save(commit=False)
            resume.user = request.user
            resume.save()

            education = education_form.save(commit=False)
            education.resume = resume
            education.save()

            experience = experience_form.save(commit=False)
            experience.resume = resume
            experience.save()

            return redirect('index')  # Redirect to success URL after successful form submission
    else:
        resume_form = ResumeForm()
        education_form = EducationForm()
        experience_form = ExperienceForm()

    return render(request, 'resume/create_resume.html', {
        'resume_form': resume_form,
        'education_form': education_form,
        'experience_form': experience_form,
    })
