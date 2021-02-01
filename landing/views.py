# from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
# from django.contrib.auth import login, logout, authenticate
from management.models import Testimonial#, InBox, About, Gallery, Facility, Team, Lecturer



def home(request):
    testis = Testimonial.objects.all().order_by('?')[:3]
    return render(request, 'index.html', {'testis':testis,})