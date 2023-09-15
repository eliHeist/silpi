# Generated by Django 4.1.3 on 2023-09-13 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='vehicles/')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
                ('condition', models.CharField(choices=[('new', 'Brand New'), ('used', 'Used')], max_length=20)),
                ('more_details', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
