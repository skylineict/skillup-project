# Generated by Django 5.0.6 on 2024-09-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_project',
            name='task_required_score',
            field=models.IntegerField(max_length=200),
        ),
    ]
