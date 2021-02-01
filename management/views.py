# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib import messages # add context to HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.utils import timezone

from .models import Testimonial, InBox, About, Gallery, Facility, Team, Lecturer
from userprofile.models import UserProfile
from userprofile.forms import UserForm, ProfileForm, RegFeeForm, TuiFeeForm
from .forms import TestimonialForm, InBoxForm

# Create your views here.
def csrf_failure(request, reason=""):
    # context_instance = {'message': 'message'}
    return render(request, 'management/csrf.html')


def index(request):
    if request.user.is_authenticated() and not request.user.is_staff:
        return HttpResponseRedirect('/user/profile/')
    else:
        CURRENTYEAR = timezone.now().today().year
        testis = Testimonial.objects.all().order_by('?')[:3]
        try:
            about = About.objects.all()[0]
        except IndexError:
            about = None
        print(testis)
        context_instance = {
        'testis':testis,
        'about':about,
        'CURRENTYEAR':CURRENTYEAR
        }
        return render(request, 'management/index.html', context_instance)

def contact(request):
    try:
        cont = About.objects.all()[0]
    except Exception:
        cont = None
    CURRENTYEAR = timezone.now().today().year
    if request.method == 'POST':
        form = InBoxForm(request.POST)
        if form.is_valid():
            msg = form.save()
            form = InBoxForm()
            context_instance = {
            'form': form,
            'cont': cont,
            'CURRENTYEAR':CURRENTYEAR,
            'error_message': 'Successful. Thank you!'
            }
            return render(request, 'management/contact.html', context_instance)
        else:
            context_instance = {
            'form': form,
            'CURRENTYEAR':CURRENTYEAR,
            'cont': cont,
            'error_message': 'Unsuccessful. Try Again.'
            }
            return render(request, 'management/contact.html', context_instance)
    form = InBoxForm()
    return render(request, 'management/contact.html', {'cont':cont, 'form':form, 'CURRENTYEAR':CURRENTYEAR})

def testimony(request):
    praise_list = Testimonial.objects.all().order_by('-date_passed')
    # blog_list = BlogPost.objects.filter(publish=True).order_by('-publish_date')
    paginator = Paginator(praise_list, 6) # Show 6 per page
    page = request.GET.get('page')
    testimonies = paginator.get_page(page)  
    # print(testimonies)
    # CURRENTYEAR = timezone.now().today().year
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = TestimonialForm()
            context_instance = {
            'form': form,
            'object_list': testimonies,
            # 'CURRENTYEAR':CURRENTYEAR,
            'error_message': 'Successful Upload. Thank you!'
            }
            return render(request, 'management/testimony.html', context_instance)
        else:
            context_instance = {
            'form': form, 
            'object_list': testimonies,
            # 'CURRENTYEAR':CURRENTYEAR,
            'error_message': 'Unsuccessful Upload. Try Again.'
            }
            return render(request, 'management/testimony.html', context_instance)
    form = TestimonialForm()
    context={
        'form' : form, 
        'object_list': testimonies, 
        # 'CURRENTYEAR':CURRENTYEAR
        }
    return render(request, 'management/testimony.html', context)

def about(request):
    try:
        about = About.objects.all()[0]
    except:
        about = None
    team_list = Team.objects.all().order_by('?')
    paginator = Paginator(team_list, 6) # Show 6 per page
    page = request.GET.get('page')
    teams = paginator.get_page(page)  

    return render(request, 'management/about.html', {'about':about, 'object_list':teams})


def login_user(request):
    CURRENTYEAR = timezone.now().today().year
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    userprofile = UserProfile.objects.get(user=request.user)
                except UserProfile.DoesNotExist:
                    context_instance= {'error_message': 'Enter valid details or Create an account'}
                    return render(request, 'management/login.html', context_instance)
                return render(request, 'userprofile/profile.html', {'userprofile':userprofile, 'CURRENTYEAR':CURRENTYEAR})
            else:
                context_instance= {'error_message': 'Your account has been disabled'}
                return render(request, 'management/login.html', context_instance)
        else:
            context_instance = {'error_message': 'Invalid Username or Password'}
            return render(request, 'management/login.html', context_instance)
    return render(request, 'management/login.html', {'CURRENTYEAR':CURRENTYEAR,})

def logout_user(request):
    if  not request.user.is_authenticated():
        return render(request, 'management/login.html',)
    logout(request)
    return render(request, 'management/login.html')

def team(request):
    team = Team.objects.all()
    CURRENTYEAR = timezone.now().today().year
    return render(request, 'management/team.html', {'team':team, 'CURRENTYEAR':CURRENTYEAR})

def team_member(request, team_id):
    t = get_object_or_404(Team, pk=team_id)
    CURRENTYEAR = timezone.now().today().year
    return render(request, 'management/team_member.html', {'t':t, 'CURRENTYEAR':CURRENTYEAR})

def gallery(request):
    gal = Gallery.objects.all()
    CURRENTYEAR = timezone.now().today().year
    return render(request, 'management/gallery.html', {'gal':gal, 'CURRENTYEAR':CURRENTYEAR})

def facilities(request):
    faci = Facility.objects.all()
    CURRENTYEAR = timezone.now().today().year
    return render(request, 'management/facilities.html', {'faci':faci, 'CURRENTYEAR':CURRENTYEAR})

def lecturers(request):
    lect_list = Lecturer.objects.all().order_by('?')
    paginator = Paginator(lect_list, 6) # Show 6 per page
    page = request.GET.get('page')
    lecturers = paginator.get_page(page) 
    return render(request, 'management/lecturers.html', {'object_list':lecturers,})

def lecturer(request, lecturer_id):
    t = get_object_or_404(Lecturer, pk=lecturer_id)
    return render(request, 'management/lecturer.html', {'t':t,})