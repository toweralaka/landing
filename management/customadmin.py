from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as OldFlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm as FlatpageFormOld
from django.utils.translation import gettext_lazy as _

from .models import About


class AboutForm(FlatpageFormOld):
    directions = forms.CharField(widget=CKEditorUploadingWidget())
    vision = forms.CharField(widget=CKEditorUploadingWidget())
    mission = forms.CharField(widget=CKEditorUploadingWidget())
    story = forms.CharField(widget=CKEditorUploadingWidget())
    greeting = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = About
        fields = '__all__'



class AboutAdmin(OldFlatPageAdmin):
    form = AboutForm
    fieldsets = (
        (None, {'fields': ('sites', 'url', 'title', 'logo', 'name', 
            'motto', 'address', 'directions', 'website', 'email', 
            'mission', 'story', 'head', 'greeting',
            'twitter', 'facebook', 'linkedin', 'instagram', 
            'phone', 'vision', 'greeting_image' 
                            )}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )
