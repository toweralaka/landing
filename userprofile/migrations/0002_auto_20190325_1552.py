# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-03-25 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.PositiveIntegerField(help_text='Registration Fee')),
                ('base_fee', models.PositiveIntegerField()),
                ('course_fee', models.PositiveIntegerField(help_text='Fee Per Course')),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Examination')),
            ],
        ),
        migrations.RenameField(
            model_name='registrationfee',
            old_name='amount',
            new_name='amount_paid',
        ),
        migrations.RenameField(
            model_name='tuitionfee',
            old_name='amount',
            new_name='amount_paid',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='empoyers_name',
            new_name='employers_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='paid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='registrationfee',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='tuitionfee',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='current_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.Level', verbose_name='Level to be attempted'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_passed',
            field=models.DateField(null=True, verbose_name='Date last level was passed/exempted'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.Examination'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='exam_date',
            field=models.DateField(null=True, verbose_name='Expected date of coming exam'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last-level+', to='userprofile.Level', verbose_name='Last level passed/exempted'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sponsor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='level',
            unique_together=set([('name', 'rank', 'exam')]),
        ),
        migrations.AddField(
            model_name='paymentstructure',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.Level'),
        ),
        migrations.AlterUniqueTogether(
            name='paymentstructure',
            unique_together=set([('examination', 'level')]),
        ),
    ]
