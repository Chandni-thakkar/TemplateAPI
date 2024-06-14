from django.db import models

class User(models.Model):
    email = models.EmailField()
    email_type = models.CharField(max_length=255)
    total_visitors = models.IntegerField()
    visit_link = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=100)
    visit_request_number = models.CharField(max_length=50)
    visit_cancelled_stage_reason = models.CharField(max_length=200, blank=True)
    visit_start_time = models.CharField(max_length=20)
    recipient_name = models.CharField(max_length=100)
    type_of_visit = models.CharField(max_length=20)
    visit_end_time = models.CharField(max_length=20)
    visit_start_date = models.CharField(max_length=20)

class Template(models.Model):
    template_version = models.IntegerField()
    channel = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
