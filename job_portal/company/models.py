from django.db import models
from django.core.validators import MaxValueValidator, FileExtensionValidator
from accounts.models import User
from .validators import size_validator

# Create your models here.

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to='company_logo', validators=[FileExtensionValidator(['pdf', 'png']), size_validator])
    established_date = models.CharField(max_length = 100 )
    address = models.CharField(max_length = 300 )
    license_image = models.ImageField(upload_to='company_license', validators=[FileExtensionValidator(['pdf', 'png']), size_validator])
    company_email = models.EmailField(max_length =100)
    company_website = models.URLField(max_length= 100, required=False )
    company_detail = models.TextField(max_length= 10000, required=False)


