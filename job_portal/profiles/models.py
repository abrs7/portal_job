from typing import Any
from django.db import models
from django.core.validators import MaxValueValidator, FileExtensionValidator, RegexValidator
from accounts.models import User

from .validators import size_validator

# Create your models here.

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100, blank=False)
    logo = models.ImageField(default='none' ,upload_to='company_logo/', validators=[FileExtensionValidator(['pdf', 'png', 'jpg']), size_validator])
    established_date = models.CharField(max_length = 100 )
    address = models.CharField(max_length = 300 )
    license_image = models.ImageField(default='none' ,upload_to='company_license/', validators=[FileExtensionValidator(['pdf', 'png','jpg']), size_validator])
    company_email = models.EmailField(max_length =100)
    company_website = models.URLField(max_length= 100 )
    company_detail = models.TextField(max_length= 10000)
    slug = models.PositiveIntegerField(unique=True, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            
            max_slug = CompanyProfile.objects.all().aggregate(models.Max('slug'))['slug__max']
            if max_slug is None:
                max_slug = 0
            
            self.slug = max_slug + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"user: {self.user}, name: {self.name}"
    
class ContractorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 100, blank=False)
    last_name = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to='company_logo', validators=[FileExtensionValidator(['pdf', 'png']), size_validator])
    address = models.CharField(max_length = 300 )
    personal_email = models.EmailField(max_length =100)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            max_slug = ContractorProfile.objects.all().aggregate(models.Max('slug'))['slug__max']
            if max_slug is None:
                max_slug = 0

            self.slug = max_slug + 1
        super().save(*args, **kwargs)

            

    def __str__(self):
        return f"user: {self.user}, name: {self.first_name}"    

