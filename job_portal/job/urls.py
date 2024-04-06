from django.urls import path 
from . import views

urlpatterns = [

   path('job_post', views.create_job, name='create_job'),
   path('contract_post', views.create_contract, name='create_contract'),



]
