from django.contrib.auth.models import User
from django import forms

from .models import UserProfile, Examination, RegistrationFee, TuitionFee


YEAR_CHOICES = ('2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', 
    '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024')

class UserForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Re-type Password', widget=forms.PasswordInput)
    #email = forms.EmailField()
    username = forms.CharField(label='Email', error_messages = {'unique': 'A user with that Username already exists, '
        'try another'
            })
    
    class Meta:
        model = User
        
        fields = ['username', 'password1', 'password2']
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The Passwords don't match")
        return password2


class ProfileForm(forms.ModelForm):
    date_passed = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(attrs={
        'type': 'date',
        'placeholder': 'dd/mm/yy'
    }))
    exam_date = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(attrs={
        'type': 'date',
        'placeholder': 'dd/mm/yy'
    }))
    #email=(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    
    class Meta:
        model = UserProfile
        exclude = ['user', 'reg_date', 'email', 'paid']     

     # ['username', 'email', 'password1', 'password2','passport',
     #     'other_names', 'reg_no', 'empoyers_name', 'contact_address', 'contacts_details', 'exam',
     #      'last_level', 'date_passed', 'current_level', 'exam_date', 'courses', 'sponsor', 
     #      'sponsor_signature', 'institutions', 'surname', 'phone']

    def clean_phone(self):
        # Check that phone number is valid
        phone = self.cleaned_data.get("phone")
        if phone:
            try:
                int(phone) + 1
            except Exception as e:
                raise forms.ValidationError("Invalid Phone Number")
        return phone

    def clean_passport(self):
        passport = self.cleaned_data.get('passport',None)
        if not passport:
            raise forms.ValidationError("Couldn't read uploaded image")
        # if passport._height < 50 or passport._width < 50:
        #     raise forms.ValidationError("Photo dimensions are too small (minimum 50X50 )")
        if passport._size > 1*1024*1024:
            raise forms.ValidationError("Image file too large (1mb max )")

        return passport


class RegFeeForm(forms.ModelForm):
    payment_date = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(attrs={
        'type': 'date',
        'placeholder': 'dd/mm/yy'
    }))
    class Meta:
        model = RegistrationFee
        exclude = ('user', 'balance')


class TuiFeeForm(forms.ModelForm):
    payment_date = forms.DateField(input_formats=['%d/%m/%Y'], widget=forms.DateInput(attrs={
        'type': 'date',
        'placeholder': 'dd/mm/yy'
    }))
    class Meta:
        model = TuitionFee
        exclude = ('user', 'balance')



class SubjectForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('courses',)

    def clean(self):
        cleaned_data = super(SubjectForm, self).clean()
        courses = cleaned_data.get("courses")
        if courses:
            s = courses[0]
            exam = s.level
            count = 0
            for sub in courses:
                count += 1
            if count > exam.subjects:
                raise forms.ValidationError("You can't choose above the required number of subjects")



class UpdateProfileForm(forms.ModelForm):
    #examination = forms.ModelChoiceField(queryset=Examination.objects.filter(active=True), widget=forms.Select())

    class Meta:
        model = UserProfile
        fields = ('email', 'phone', 'passport')


    def clean_phone(self):
        # Check that phone number is valid
        phone = self.cleaned_data.get("phone")
        if phone:
            try:
                int(phone) + 1
            except Exception as e:
                raise forms.ValidationError("Invalid Phone Number")
        return phone


    def clean_passport(self):
        # Check that passport is valid
        picture = self.cleaned_data.get("passport",None)
        if not picture:
            raise forms.ValidationError("Couldn't read uploaded image")
        if picture.size > 250*1024:
            raise forms.ValidationError("Image file too large (250kb max)")
        if picture.size < 25*1024:
            raise forms.ValidationError("Image file too small (25kb min)")
        return picture
