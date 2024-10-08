# Generated by Django 5.1 on 2024-09-17 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSettingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('smpt_server', models.CharField(max_length=50)),
                ('smpt_port', models.PositiveIntegerField()),
                ('smpt_username', models.CharField(max_length=50)),
                ('smpt_password', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=180)),
                ('url_logo', models.CharField(max_length=50)),
                ('app_setting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_app_id', to='school.appsettingmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
