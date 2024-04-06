from django.urls import path 
from . import views

urlpatterns = [
    path('company_profile', views.company_profile, name='company_profile'),
    path('contractor_profile', views.contractor_profile, name='contractor_profile'),
    
    path('edit_profile/<slug:slug>/', views.Company_Update.as_view(), name='edit_profile'),
    path('edit_contractor/<slug:slug>/', views.Contractor_Update.as_view(), name='contractor_edit'),
    path('show_company/<slug:user_slug>/',views.show_profile, name='show_company'),
    path('show_contractor/<slug:user_slug>/',views.show_contractor, name='show_contractor'),
]
