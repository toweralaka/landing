from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    # path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('testimonial', views.testimony, name='testimony'),
    path('about-us', views.about, name='about'),
    #path('register', views.register, name='register'),
    #path('login', views.login_user, name='login'),
    path('team', views.team, name='team'),
    path('<int:team_id>/team', views.team_member, name='team_member'),
    path('lecturers', views.lecturers, name='lecturers'),
    path('<int:lecturer_id>/lecturer', views.lecturer, name='lecturer'),
    path('gallery', views.gallery, name='gallery'),
    path('facilities', views.facilities, name='facilities'),
    #path('logout', views.logout_user, name='logout'),
]