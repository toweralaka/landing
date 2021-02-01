from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('profileupdate', views.profileupdate, name='profileupdate'),
]