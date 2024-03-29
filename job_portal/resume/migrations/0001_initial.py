# Generated by Django 5.0.1 on 2024-03-28 22:18

import datetime
import django.core.validators
import django.db.models.deletion
import resume.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(1900, 1, 1), message='Birth date cannot be earlier than 1900-01-01'), django.core.validators.MaxValueValidator(limit_value=datetime.date(2006, 4, 3), message='You must be at least 18 years old')])),
                ('occupation', models.CharField(max_length=100)),
                ('bio', models.TextField(validators=[django.core.validators.MaxLengthValidator(limit_value=3000, message='Bio should not exceed 3000 characters')])),
                ('profile_picture', models.ImageField(blank=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png']), resume.validators.validate_file_size])),
                ('cv', models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx']), resume.validators.validate_file_size])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('job_description', models.TextField(validators=[django.core.validators.MaxLengthValidator(limit_value=3000, message='description should not exceed 3000 characters')])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='resume.resume')),
            ],
        ),
    ]
