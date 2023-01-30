from django.db import models

class Members(models.Model):
  name = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  student_id = models.CharField(max_length=255)
  start_time = models.CharField(max_length=255)
  end_time = models.CharField(max_length=255)
  line = models.CharField(max_length=255)
  surgery = models.CharField(max_length=255)
  internal = models.CharField(max_length=255)
  pediatrics = models.CharField(max_length=255)
  gynocology = models.CharField(max_length=255)
  ortopedix_one = models.CharField(max_length=255)
  ortopedix_two = models.CharField(max_length=255)
  urology_one = models.CharField(max_length=255)
  urology_two = models.CharField(max_length=255)
  minor_week_one = models.CharField(max_length=255)
  minor_week_two = models.CharField(max_length=255)
  minor_week_three = models.CharField(max_length=255)
  minor_month_one = models.CharField(max_length=255)
  minor_month_two = models.CharField(max_length=255)
  minor_month_three = models.CharField(max_length=255)
  pack_one = models.CharField(max_length=255)
  pack_two = models.CharField(max_length=255)
  pack_three = models.CharField(max_length=255)

class Capacity(models.Model):
    line = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)
    full = models.CharField(max_length=255)
    remain = models.CharField(max_length=255)

class Selection(models.Model):
    item_fa = models.CharField(max_length=255)
    item_en = models.CharField(max_length=255)
    choice = models.CharField(max_length=255)
    iden = models.CharField(max_length=255)
