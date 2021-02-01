# Generated by Django 3.1.1 on 2021-01-31 09:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20190325_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationfee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='userprofile.userprofile'),
        ),
        migrations.AlterField(
            model_name='tuitionfee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='userprofile.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='current_level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='current_level', to='userprofile.level', verbose_name='Level to be attempted'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_passed',
            field=models.DateField(default=datetime.datetime(2021, 1, 31, 9, 17, 38, 683134, tzinfo=utc), verbose_name='Date last level was passed/exempted'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='exam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='userprofile.examination'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='exam_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 31, 9, 18, 4, 165870, tzinfo=utc), verbose_name='Expected date of coming exam'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='last_level', to='userprofile.level', verbose_name='Last level passed/exempted'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='other_names',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sponsor',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='surname',
            field=models.CharField(max_length=250),
        ),
    ]