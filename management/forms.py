from django import forms
from django.contrib.admin.widgets import AdminDateWidget
import datetime

from .models import InBox, Testimonial, AcademicYear

YEAR_CHOICES = ('2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007',
 '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021')


    
class TestimonialForm(forms.ModelForm):
    testimonial = forms.CharField(widget=forms.Textarea(attrs={'maxlength':'400',}))
    date_passed = forms.DateField(widget=AdminDateWidget(attrs={'placeholder':'YYYY-MM-DD',}))
    #forms.DateField(widget=forms.SelectDateWidget(years=YEAR_CHOICES))
    #date_passed = forms.ModelChoiceField(queryset=AcademicYear.objects.all(), widget=forms.Select())

    class Meta():
        model = Testimonial
        exclude = ['date',]

    # def clean_picture(self):
    #     picture = self.cleaned_data.get('picture',None)
    #     if not picture:
    #         raise forms.ValidationError("Couldn't read uploaded image")
    #     if picture._height < 50 or picture._width < 50:
    #         raise forms.ValidationError("Photo dimensions are too small (minimum 50X50 )")
    #     if picture._size > 1*1024*1024:
    #         raise forms.ValidationError("Image file too large (1mb max )")

    #     return picture
    def clean_passport(self):
        passport = self.cleaned_data.get('passport',None)
        if not passport:
            raise forms.ValidationError("Couldn't read uploaded image")
        if passport.size > 1*1024*1024:
            raise forms.ValidationError("Image file too large (1mb max )")

        return passport

    
class InBoxForm(forms.ModelForm):

    class Meta():
        model = InBox
        exclude = ['date',]