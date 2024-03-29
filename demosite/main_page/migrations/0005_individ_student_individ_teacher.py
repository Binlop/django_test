# Generated by Django 5.0.1 on 2024-02-01 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_individ_count_blood_individ_count_chorion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='individ',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='main_page.student'),
        ),
        migrations.AddField(
            model_name='individ',
            name='teacher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='main_page.teacher'),
        ),
    ]
