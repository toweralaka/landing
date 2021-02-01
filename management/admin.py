# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django import forms
from .models import About, Team, Facility, Gallery, Testimonial, Event, InBox, Lecturer, AcademicYear
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from .customadmin import AboutAdmin

class TeamAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    remarks = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Team
        fields = ('name', 'position', 'picture', 'description', 'remarks')


class TeamAdmin(admin.ModelAdmin):
    forms = TeamAdminForm


class AboutAdminForm(forms.ModelForm):
    directions = forms.CharField(widget=CKEditorUploadingWidget())
    vision = forms.CharField(widget=CKEditorUploadingWidget())
    mission = forms.CharField(widget=CKEditorUploadingWidget())
    story = forms.CharField(widget=CKEditorUploadingWidget())
    greeting = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = About
        fields = ('logo', 'name', 'motto', 'address', 'directions', 'website', 'email', 'mission', 'story', 'head', 'greeting',
            'twitter', 'facebook', 'linkedin', 'instagram', 'phone', 'vision', 'greeting_image')


# class AboutAdmin(admin.ModelAdmin):
#     forms = AboutAdminForm


class LecturerAdminForm(forms.ModelForm):
    # name = models.CharField(max_length=200)
    # position = models.CharField(max_length=200, verbose_name='Course')
    # picture = models.ImageField(upload_to='team/%Y/%m/%d', help_text=("Maximum of 1mb.(400x300px)"))
    description = forms.CharField(widget=CKEditorUploadingWidget())
    remarks = forms.CharField(widget=CKEditorUploadingWidget())
    # twitter = models.CharField(max_length=100, blank=True, null=True)
    # facebook = models.CharField(max_length=100, blank=True, null=True)
    # linkedin = models.CharField(max_length=100, blank=True, null=True)
    # instagram = models.CharField(max_length=100, blank=True, null=True)
    # phone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        model = (Lecturer)
        fields = ('__all__')


class LecturerAdmin(admin.ModelAdmin):
    forms = LecturerAdminForm


class EventAdminForm(forms.ModelForm):
    # date = models.DateTimeField(auto_now_add=True)
    # name = models.CharField(max_length=50)
    # email = models.EmailField()
    # subject = models.CharField(max_length=50)
    message = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        models = Event
        fields = ('__all__')


class EventAdmin(admin.ModelAdmin):
    forms = EventAdminForm

class InBoxAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'subject', 'message', 'date',)
    list_display = ('name', 'email', 'subject', 'message', 'date',)


class TestimonialAdmin(admin.ModelAdmin):
    fields = ('name', 'exam', 'reg_number', 'date_passed', 'testimonial',)
    list_display = ('name', 'exam', 'reg_number', 'date_passed', 'testimonial', 'date',)
    #search_fields = ('name', 'state',)


class myForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ('__all__')

    def clean_picture(self):
        picture = self.cleaned_data.get("picture")
        if not picture:
            raise forms.ValidationError("No image!")
        else:
            #w, h = get_image_dimensions(picture)
            w = picture.width
            h = picture.height
            if w > 800:
                raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 800px" % w)
            if h > 600:
                raise forms.ValidationError("The image is %i pixel high. It's supposed to be 600px" % h)
        return picture

class FacilityAdmin(admin.ModelAdmin):
    forms = myForm


# class myForm(forms.ModelForm):
#    class Meta:
#        model = myModel
#    def clean_picture(self):
#        picture = self.cleaned_data.get("picture")
#        if not picture:
#            raise forms.ValidationError("No image!")
#        else:
#            w, h = get_image_dimensions(picture)
#            if w != 100:
#                raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 100px" % w)
#            if h != 200:
#                raise forms.ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)
#        return picture

# class MyAdmin(admin.ModelAdmin):
#     form = myForm

# admin.site.register(Example, MyAdmin)

# Register your models here.
admin.site.register(About, AboutAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Facility)
admin.site.register(Gallery)
admin.site.register(AcademicYear)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(InBox, InBoxAdmin)