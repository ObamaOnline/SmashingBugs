# Generated by Django 4.0.4 on 2022-05-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_result_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='scan',
            field=models.FileField(blank=True, default=None, null=True, upload_to='test'),
        ),
    ]
