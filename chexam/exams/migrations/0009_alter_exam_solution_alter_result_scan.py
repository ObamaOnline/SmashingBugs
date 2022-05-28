# Generated by Django 4.0.4 on 2022-05-28 02:05

from django.db import migrations, models
import exams.models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_alter_problem_scan_alter_result_scan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='solution',
            field=models.FileField(blank=True, default=None, upload_to='Solutions'),
        ),
        migrations.AlterField(
            model_name='result',
            name='scan',
            field=models.FileField(blank=True, default=None, upload_to=exams.models.folder_name),
        ),
    ]