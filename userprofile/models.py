# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save


import datetime


class Examination(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField()
    picture = models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length = 20)
    abbr = models.CharField(max_length = 10)
    rank = models.IntegerField(unique = True)
    exam = models.ForeignKey(Examination, on_delete=models.CASCADE)
    no_courses = models.IntegerField(default = 1)

    class Meta:
        unique_together = ('name', 'rank', 'exam')

    def __str__(self):
        return self.name


class Course(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    abbr = models.CharField(max_length=10)

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    SEX = (
        ('F', 'female'),
        ('M', 'male'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    passport = models.ImageField(upload_to="photos/%Y/%m/%d", help_text=("Maximum of 1mb.(100x100px)"))
    surname = models.CharField(max_length = 250)
    other_names = models.CharField(max_length = 250)
    reg_no = models.CharField(max_length = 20)
    email = models.EmailField()
    sex = models.CharField(max_length=1, choices=SEX)
    phone = models.CharField(max_length = 13)
    employers_name = models.CharField(max_length =50)
    contact_address = models.TextField()
    contacts_details = models.TextField(
        "In case of emergency, contact person NAME, ADDRESS, PHONE")
    institutions = models.TextField("Schools attended till date")
    exam = models.ForeignKey(Examination, on_delete=models.PROTECT)
    last_level = models.ForeignKey(
        Level, on_delete=models.PROTECT, related_name='last_level', 
        verbose_name="Last level passed/exempted")
    date_passed = models.DateField(verbose_name ="Date last level was passed/exempted")
    current_level = models.ForeignKey(
        Level, on_delete=models.PROTECT, related_name='current_level', 
        verbose_name="Level to be attempted")
    exam_date = models.DateField(verbose_name ="Expected date of coming exam")
    courses = models.ManyToManyField(Course)
    sponsor = models.CharField(max_length = 250)
    sponsor_signature = models.ImageField(
        upload_to="photos/%Y/%m/%d", help_text=("Maximum of 1mb.(100x100px)"))
    reg_date = models.DateTimeField(auto_now_add = True)
    paid = models.BooleanField(default=True)

    def __str__(self):
        return self.user
    

class PaymentStructure(models.Model):
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    registration = models.PositiveIntegerField(help_text='Registration Fee')
    base_fee = models.PositiveIntegerField()
    course_fee = models.PositiveIntegerField(help_text='Fee Per Course')

    class Meta:
        unique_together = ('examination', 'level')

    def __str__(self):
        return str(self.level)



class RegistrationFee(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    amount_paid = models.PositiveIntegerField()
    payment_date = models.DateField()
    teller_no = models.CharField(max_length=10)
    balance = models.PositiveIntegerField()

    def __str__(self):
        return self.user


class TuitionFee(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    amount_paid = models.PositiveIntegerField()
    payment_date = models.DateField()
    teller_no = models.CharField(max_length=10)
    balance = models.PositiveIntegerField()

    def __str__(self):
        return str(self.user)

