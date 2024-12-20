# Generated by Django 5.1.3 on 2024-11-28 15:35

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultancyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
                ('client_name', models.CharField(blank=True, max_length=100, null=True)),
                ('project_date', models.DateField()),
                ('services_offered', models.CharField(max_length=200)),
                ('project_duration', models.CharField(max_length=50)),
                ('project_location', models.CharField(max_length=100)),
            ],
        ),
    ]
