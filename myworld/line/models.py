from django.db import models

class Members(models.Model):
  name = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  student_id = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  start_time = models.CharField(max_length=255)
  end_time = models.CharField(max_length=255)
  line = models.CharField(max_length=255)
  health_dermatology_ent_one = models.CharField(max_length=255)
  health_dermatology_ent_two = models.CharField(max_length=255)
  health_dermatology_ent_three = models.CharField(max_length=255)
  anesthesia_emergency_ophthalmology_one = models.CharField(max_length=255)
  anesthesia_emergency_ophthalmology_two = models.CharField(max_length=255)
  anesthesia_emergency_ophthalmology_three = models.CharField(max_length=255)
  neurology_psychiatry_infectious_one = models.CharField(max_length=255)
  neurology_psychiatry_infectious_two = models.CharField(max_length=255)
  neurology_psychiatry_infectious_three = models.CharField(max_length=255)
  ethics_radiology_one = models.CharField(max_length=255)
  ethics_radiology_two = models.CharField(max_length=255)
  orthopedics_urology_one = models.CharField(max_length=255)
  orthopedics_urology_two = models.CharField(max_length=255)
  internal = models.CharField(max_length=255)
  surgery = models.CharField(max_length=255)
  gynecology = models.CharField(max_length=255)
  pediatric = models.CharField(max_length=255)

class Capacity(models.Model):
    line = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)
    full = models.CharField(max_length=255)
    remain = models.CharField(max_length=255)

class Selection(models.Model):
    item = models.CharField(max_length=255)
    choice = models.CharField(max_length=255)
