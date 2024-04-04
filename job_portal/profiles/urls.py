from django.urls import path 
from . import views

urlpatterns = [
    path('company_profile', views.company_profile, name='company_profile'),
    path('contractor_profile', views.contractor_profile, name='contractor_profile'),
    path('job_post', views.job_creation, name='job_post'),
]