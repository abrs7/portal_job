# Generated by Django 5.0.1 on 2024-04-06 14:13

import django.core.validators
import django.utils.timezone
import profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_companyprofile_license_image_companyprofile_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractorprofile',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='license_image',
            field=models.ImageField(default='none', upload_to='company_license/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'png', 'jpg']), profiles.validators.size_validator]),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='logo',
            field=models.ImageField(default='none', upload_to='company_logo/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'png', 'jpg']), profiles.validators.size_validator]),
        ),
    ]
