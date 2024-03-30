from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, FileExtensionValidator
from datetime import date, timedelta
from accounts.models import User
from .validators import validate_file_size



class Resume(models.Model):

    max_birth_date = date.today() - timedelta(days=18*365)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(validators=[
        MinValueValidator(limit_value=date(1900, 1, 1), message='Birth date cannot be earlier than 1900-01-01'),
        MaxValueValidator(limit_value=max_birth_date, message='You must be at least 18 years old')
    ])
    occupation = models.CharField(max_length=100)
    # education = models.CharField(max_length=100)
    # experience = models.CharField(max_length=300, blank=True)
    bio = models.TextField(validators=[MaxLengthValidator(limit_value=3000, message='Bio should not exceed 3000 characters')])
    profile_picture = models.ImageField(upload_to='media/images/', blank=True, 
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png']), validate_file_size])  # 5 MB limit
    cv = models.FileField(
        upload_to='files/', validators=[FileExtensionValidator(['pdf', 'docx']), validate_file_size])  # 5 MB limit

    def __str__(self):
        return f"{self.first_name} {self.last_name}'s Resume"

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_description = models.TextField(validators=[MaxLengthValidator(limit_value=3000, message='description should not exceed 3000 characters')])
    start_date = models.DateField()
    end_date = models.DateField()