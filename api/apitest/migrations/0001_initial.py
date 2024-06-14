# Generated by Django 4.2.13 on 2024-06-12 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_id', models.CharField(max_length=255, unique=True)),
                ('template_version', models.IntegerField()),
                ('channel', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('email_type', models.CharField(max_length=255)),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apitest.template')),
            ],
        ),
        migrations.CreateModel(
            name='BodyVar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_visitors', models.IntegerField()),
                ('visit_link', models.CharField(max_length=255)),
                ('organization_name', models.CharField(max_length=255)),
                ('visit_request_number', models.CharField(max_length=255)),
                ('visit_cancelled_stage_reason', models.CharField(blank=True, max_length=255)),
                ('visit_start_time', models.TimeField()),
                ('recipient_name', models.CharField(max_length=255)),
                ('type_of_visit', models.CharField(max_length=255)),
                ('visit_end_time', models.TimeField()),
                ('visit_start_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apitest.user')),
            ],
        ),
    ]
