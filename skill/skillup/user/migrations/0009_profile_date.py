# Generated by Django 5.0.6 on 2024-07-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
