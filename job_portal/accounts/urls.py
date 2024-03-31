from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('login', views.login, name='login'),
    path('candidate_register', views.candidate_register, name='candidate_register'),
    path('company_register', views.company_register, name='company_register'),
    path('contractor_register', views.contractor_register, name='contractor_register'),
    # path('home-candidate', views.home_candidate, name='home_candidate'),
    path('home_candidate', views.home_candidate, name='home_candidate'),
    path('home_company', views.home_company, name='home_company'),
    path('home_contractor', views.home_contractor, name='home_contractor'),
     path('logout/', views.LogOutView, name='logout'),

]
