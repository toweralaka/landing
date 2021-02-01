# Generated by Django 3.1.1 on 2021-01-31 09:18

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0004_auto_20210131_1018'),
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('flatpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='flatpages.flatpage')),
                ('logo', models.ImageField(help_text='Maximum of 1mb.(100x100px)', upload_to='about/logo/%Y/%m/%d')),
                ('name', models.CharField(max_length=100)),
                ('motto', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('directions', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('website', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('linkedin', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('phone1', models.CharField(max_length=13)),
                ('phone2', models.CharField(blank=True, max_length=13)),
                ('phone3', models.CharField(blank=True, max_length=13)),
                ('phone4', models.CharField(blank=True, max_length=13)),
                ('vision', ckeditor_uploader.fields.RichTextUploadingField()),
                ('mission', ckeditor_uploader.fields.RichTextUploadingField()),
                ('story', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('head', models.CharField(max_length=50)),
                ('greeting', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('greeting_image', models.ImageField(blank=True, help_text='Maximum of 1mb.(100x100px)', upload_to='about/%Y/%m/%d')),
            ],
            options={
                'verbose_name_plural': 'About',
            },
            bases=('flatpages.flatpage',),
        ),
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('event', models.CharField(max_length=50)),
                ('picture', models.ImageField(help_text='Maximum of 1mb.(1200x900px)', upload_to='event/%Y/%m/%d')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('picture', models.ImageField(help_text='Maximum of 1mb.(1200x900px)', upload_to='facil/%Y/%m/%d')),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('picture', models.ImageField(help_text='Maximum of 1mb.(1200x900px)', upload_to='galle/%Y/%m/%d')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='InBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name_plural': 'InBoxes',
            },
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200, verbose_name='Course')),
                ('picture', models.ImageField(help_text='Maximum of 1mb.(400x300px)', upload_to='team/%Y/%m/%d')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('remarks', ckeditor_uploader.fields.RichTextUploadingField()),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=200)),
                ('picture', models.ImageField(help_text='Maximum of 1mb.(400x300px)', upload_to='team/%Y/%m/%d')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('remarks', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reg_number', models.CharField(max_length=50)),
                ('date_passed', models.DateField()),
                ('testimonial', models.TextField()),
                ('passport', models.ImageField(help_text='Maximum of 1mb.(250x250px)', upload_to='testim/%Y/%m/%d')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userprofile.examination')),
            ],
            options={
                'unique_together': {('reg_number', 'date_passed')},
            },
        ),
    ]