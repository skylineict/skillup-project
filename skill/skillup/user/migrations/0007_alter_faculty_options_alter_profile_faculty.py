# Generated by Django 5.0.6 on 2024-06-26 23:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_faculty_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': 'Faculty', 'verbose_name_plural': 'Faculties'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faculties', to='user.faculty'),
        ),
    ]
