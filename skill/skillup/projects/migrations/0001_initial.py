# Generated by Django 5.0.6 on 2024-09-07 21:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cohorts', '0002_rename_cohort_cohortgroup'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('task_required_score', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'completed'), ('progress', 'progress')], default='pending', max_length=20)),
                ('cohort', models.ManyToManyField(related_name='tasks', to='cohorts.cohortgroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_url', models.URLField(blank=True, null=True)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='projects.student_project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
