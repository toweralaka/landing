# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import UserProfile, RegistrationFee, TuitionFee, Course, Level, Examination
# Register your models here.



class TuitionFeeInline(admin.StackedInline):
    model = TuitionFee


class RegistrationFeeInline(admin.StackedInline):
    model = RegistrationFee


class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'reg_no', 'exam', 'reg_date',)
	list_filter = ('reg_date', 'exam',)
	search_fields = ('first_name', 'last_name', 'reg_no', 'phone',)

	inlines = [RegistrationFeeInline, TuitionFeeInline]



class RegistrationFeeAdmin(admin.ModelAdmin):
    list_display = ('user',)
    fields = ('user',)



admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(RegistrationFee, RegistrationFeeAdmin)
admin.site.register(TuitionFee)
admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Examination)