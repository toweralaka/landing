# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField 
from django.contrib.auth.models import User, Group, Permission
from django.contrib.flatpages.models import FlatPage as FlatPageOld
from django.db import models
from django.db.models.signals import post_save, pre_save, post_init
from django.utils.safestring import mark_safe

from userprofile.models import Examination


# Create your models here.


class About(FlatPageOld):
    logo = models.ImageField(
        upload_to='about/logo/%Y/%m/%d', help_text=("Maximum of 1mb.(100x100px)"))
    name = models.CharField(max_length=100)
    motto = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    directions = RichTextUploadingField(blank = True, null = True)
    website = models.CharField(max_length=30)
    email = models.EmailField()
    twitter = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=250, help_text="Separate with comma")
    # phone2 = models.CharField(max_length=13, blank=True)
    # phone3 = models.CharField(max_length=13, blank=True)
    # phone4 = models.CharField(max_length=13, blank=True)
    vision = RichTextUploadingField()
    mission = RichTextUploadingField()
    story = RichTextUploadingField(blank=True, null=True)
    head = models.CharField(max_length=50)
    greeting = RichTextUploadingField(blank=True)
    greeting_image = models.ImageField(
        blank=True, upload_to='about/%Y/%m/%d', help_text=("Maximum of 1mb.(100x100px)"))

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.name


class AcademicYear(models.Model):
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.year

class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    picture = models.ImageField(
        upload_to='team/%Y/%m/%d', help_text=("Maximum of 1mb.(400x300px)"))
    description = RichTextUploadingField()
    remarks = RichTextUploadingField()

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, verbose_name='Course')
    picture = models.ImageField(
        upload_to='team/%Y/%m/%d', help_text=("Maximum of 1mb.(400x300px)"))
    description = RichTextUploadingField()
    remarks = RichTextUploadingField()
    twitter = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    picture = models.ImageField(
        upload_to='facil/%Y/%m/%d', help_text=("Maximum of 1mb.(1200x900px)"))

    class Meta:
        verbose_name_plural = "Facilities"

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField(
        upload_to='galle/%Y/%m/%d', help_text=("Maximum of 1mb.(1200x900px)"))
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Gallery"

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    exam = models.ForeignKey(
        Examination, on_delete=models.SET_NULL, blank=True, null=True)
    reg_number = models.CharField(max_length=50)
    date_passed = models.DateField()
    testimonial = models.TextField()
    #change to picture/photo
    passport = models.ImageField(
        upload_to='testim/%Y/%m/%d', help_text=("Maximum of 1mb.(250x250px)"))
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reg_number', 'date_passed')

    def __str__(self):
        return self.name


class Event(models.Model):
    date = models.DateTimeField()
    event = models.CharField(max_length=50)
    picture = models.ImageField(
        upload_to='event/%Y/%m/%d',help_text=("Maximum of 1mb.(1200x900px)"))
    description = RichTextUploadingField()

    def __str__(self):
        return self.event


class InBox(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "InBoxes"

    def __str__(self):
        return self.name



