# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Children(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.TextField(blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    sex = models.TextField(blank=True, null=True)  # This field type is a guess.
    mother = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'Children'


class Donations(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    date_and_time = models.DateField(blank=False, null=False)
    requested = models.TextField(blank=True, null=True)
    given = models.TextField(blank=True, null=True)
    amount = models.TextField(blank=True, null=True)  # This field type is a guess.
    mother = models.IntegerField(blank=False, null=False)
    operator = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'Donations'


class Mothers(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    surname = models.TextField(blank=False, null=False)
    name = models.TextField(blank=False, null=False)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.TextField(blank=True, null=True)
    civil_status = models.TextField(blank=True, null=True)
    residency = models.TextField(blank=True, null=True)
    origin_country = models.TextField(blank=False, null=False)
    highest_academic_achievement = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    registration_date = models.TextField(blank=False, null=False)
    husband_surname = models.TextField(blank=True, null=True)
    husband_job = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    income = models.TextField(blank=True, null=True)  # This field type is a guess.
    fixed_expenditures = models.TextField(blank=True, null=True)  # This field type is a guess.
    operator = models.IntegerField(blank=False, null=False)
    phone_1 = models.TextField(blank=True, null=True)
    phone_2 = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):

        return ' '.join([
            self.name,
            self.surname,
        ])

    class Meta:
        managed = False
        db_table = 'Mothers'


class Operators(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.TextField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'Operators'
