# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render#, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import messages # add context to HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

from userprofile.models import UserProfile
from userprofile.forms import (UserForm, ProfileForm, RegFeeForm, 
	TuiFeeForm, UpdateProfileForm)

# Create your views here.

def contact(request):
	pass


def register(request):
	CURRENTYEAR = timezone.now().today().year
	if request.method == 'POST':
		uform = UserForm(request.POST)
		pform = ProfileForm(request.POST, request.FILES)
		rform = RegFeeForm(request.POST)
		tform = TuiFeeForm(request.POST)
		if uform.is_valid() and pform.is_valid() and rform.is_valid() and tform.is_valid():
			user = uform.save(commit=False)
			username = uform.cleaned_data['username']
			password = uform.cleaned_data['password1']
			#email = uform.cleaned_data['email']
			user.set_password(password)
			user.email = username
			user.save()
			passport = pform.cleaned_data['passport']
			surname = pform.cleaned_data['surname']
			other_names = pform.cleaned_data['other_names']
			reg_no = pform.cleaned_data['reg_no']
			sex = pform.cleaned_data['sex']
			phone = pform.cleaned_data['phone']
			employers_name = pform.cleaned_data['employers_name']
			contact_address = pform.cleaned_data['contact_address']
			contacts_details = pform.cleaned_data['contacts_details']
			institutions = pform.cleaned_data['institutions']
			exam = pform.cleaned_data['exam']
			last_level = pform.cleaned_data['last_level']
			date_passed = pform.cleaned_data['date_passed']
			current_level = pform.cleaned_data['current_level']
			exam_date = pform.cleaned_data['exam_date']
			sponsor = pform.cleaned_data['sponsor']
			sponsor_signature = pform.cleaned_data['sponsor_signature']
			courses = pform.cleaned_data['courses']
			# user = authenticate(username=username, password=password)
			# if user is not None:
			#     if user.is_active:
			#         login(request, user)
			# userprofile = pform.save(commit=False)
			userprofile, created = UserProfile.objects.get_or_create(user=user)
			userprofile.email = username
			userprofile.passport = passport
			userprofile.surname = surname
			userprofile.other_names = other_names
			userprofile.reg_no = reg_no
			userprofile.sex = sex
			userprofile.phone = phone
			userprofile.employers_name = employers_name
			userprofile.contact_address = contact_address
			userprofile.contacts_details = contacts_details
			userprofile.institutions = institutions
			userprofile.exam = exam
			userprofile.last_level = last_level
			userprofile.date_passed = date_passed
			userprofile.current_level = current_level
			userprofile.exam_date = exam_date
			userprofile.sponsor = sponsor
			userprofile.sponsor_signature = sponsor_signature
			for i in courses:
				userprofile.courses.add(i)
			userprofile.save()

			regfee = rform.save(commit=False)
			regfee.user = userprofile
			regfee.save()
			tuifee = tform.save(commit=False)
			tuifee.user = userprofile
			tuifee.save()

			messages.add_message(request, messages.INFO, 
			"Registration Successful! Please Login")
			return HttpResponseRedirect('/login/')
			
		else:
			# uform = UserForm()
			# pform = ProfileForm()
			context_instance = {'uform': uform, 'pform': pform, 'CURRENTYEAR':CURRENTYEAR,
			'rform': rform, 'tform': tform, 'error_message': 'Invalid Registration!'}
			return render(request, 'userprofile/register.html', context_instance)
	else:
		uform = UserForm()
		pform = ProfileForm()
		rform = RegFeeForm()
		tform = TuiFeeForm()
		context_instance = {'uform': uform, 'pform': pform, 'rform': rform, 'tform': tform, 'CURRENTYEAR':CURRENTYEAR}
		return render(request, 'userprofile/register.html', context_instance)


def profile(request):
	CURRENTYEAR = timezone.now().today().year
	userprofile = UserProfile.objects.get(user=request.user)
	context_instance={'userprofile':userprofile, 'CURRENTYEAR':CURRENTYEAR,
	'error_message': ''}
	return render(request, 'userprofile/profile.html', context_instance)


def profileupdate(request):
    if request.user.is_authenticated() and not request.user.is_staff:
        try:
            userprofile = UserProfile.objects.get(user=request.user)
            if userprofile.paid:
                pform = UpdateProfileForm(request.POST or None, request.FILES or None, instance=userprofile)
               # sform = SubjectForm(request.POST or None, instance=userprofile)
                if request.method == 'POST':
                    if pform.is_valid():# and sform.is_valid():
                        pform.save()
                        #sform.save()
                        return HttpResponseRedirect('/user/profile/')
                context_instance={'pform': pform, 'userprofile':userprofile}
                return render(request, 'userprofile/update_profile.html', context_instance)
            else:
                logout(request)
                messages.add_message(request, messages.INFO, 
                "Your Payment Has Not Been Confirmed. Please Check Back Or Make Payment If You Have Not")
                return HttpResponseRedirect('/login/')
        except UserProfile.DoesNotExist:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')