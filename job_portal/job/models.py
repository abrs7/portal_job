from django.db import models
from profiles.models import CompanyProfile, ContractorProfile

# Create your models here.
GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]
class JobPost(models.Model):
    poster = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    position = models.CharField(max_length=256)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    description = models.CharField(max_length=4000)
    required = models.PositiveIntegerField()
    deadline = models.DateField()
    salary = models.PositiveIntegerField(blank=True)
    slug = models.SlugField(unique=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            max_slug = JobPost.objects.all().aggregate(models.Max('slug'))['slug__max']
            if max_slug is None:
                max_slug = 0

            self.slug = max_slug + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Position: {self.position}"

class ContractPost(models.Model):
    poster = models.ForeignKey(ContractorProfile, on_delete=models.CASCADE)
    position = models.CharField(max_length=256)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    description = models.CharField(max_length=4000)
    required = models.PositiveIntegerField()
    deadline = models.DateField()
    salary = models.PositiveIntegerField(blank=True)
    slug = models.SlugField(unique=True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            max_slug = ContractPost.objects.all().aggregate(models.Max('slug'))['slug__max']
            if max_slug is None:
                max_slug = 0

            self.slug = max_slug + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Position: {self.position}"    

