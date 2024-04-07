# Generated by Django 5.0.1 on 2024-04-05 21:24

import django.core.validators
import django.utils.timezone
import profiles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_companyprofile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='license_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='company_license', validators=[django.core.validators.FileExtensionValidator(['pdf', 'png', 'jpg']), profiles.validators.size_validator]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='logo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='company_logo', validators=[django.core.validators.FileExtensionValidator(['pdf', 'png', 'jpg']), profiles.validators.size_validator]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='slug',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]