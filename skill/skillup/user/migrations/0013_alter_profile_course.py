# Generated by Django 5.0.6 on 2024-08-02 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_profile_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courselist', to='user.courselist'),
        ),
    ]
