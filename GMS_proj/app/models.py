#  This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ComplaintMessage(models.Model):
    profile_id = models.IntegerField()
    message = models.CharField(max_length=255)
    media = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = True
        db_table = 'complaint_message'


class ComplaintStatus(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'complaint_status'


class CreateComplaint(models.Model):
    profile_id = models.IntegerField()
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=1000)
    current_handler = models.CharField(max_length=35)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'create_complaint'


class Department(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'department'


class Designation(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'designation'


class Profile(models.Model):
    name = models.CharField(max_length=27)
    mobile = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    profile_type_id = models.IntegerField()
    designation_id = models.IntegerField()
    department_id = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        managed = True
        db_table = 'profile'


class ProfileType(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'profile_type'


class UserRegistration(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'user_registration'