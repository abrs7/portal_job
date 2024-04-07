from django.db import models
from django.utils.text import slugify
from profiles.models import CompanyProfile, ContractorProfile

# Create your models here.

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

def generate_unique_slug(model, value, slug_field='slug'):
    """Generate a unique slug for the given model and value."""
    slug = slugify(value)
    unique_slug = slug
    extension = 1

    # Check if the generated slug already exists in the database
    while model.objects.filter(**{slug_field: unique_slug}).exists():
        unique_slug = f"{slug}-{extension}"
        extension += 1

    return unique_slug

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
            self.slug = generate_unique_slug(JobPost, self.position)
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
            self.slug = generate_unique_slug(ContractPost, self.position)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Position: {self.position}"
