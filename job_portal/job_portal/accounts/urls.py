from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('home-candidate', views.home_candidate, name='home_candidate'),
    path('home', views.home, name='home'),
    

]
