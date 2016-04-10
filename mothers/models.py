# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


def missing():
    return '~Non Disp.'


def format_text(text):
    return text.encode('utf-8') if text else missing()


def format_date(date):
    return date.strftime('%d %b %Y') if date else missing()


class Operators(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.TextField(blank=False, null=False)

    def get_absolute_url(self):
        return reverse('operator-view', kwargs={'pk': self.id})

    def get_modify_url(self):
        return reverse('operator-edit', kwargs={'pk': self.id})

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return format_text(self.name)

    class Meta:
        managed = False
        db_table = 'Operators'


class Mothers(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    surname = models.TextField(blank=False, null=False)
    name = models.TextField(blank=False, null=False)
    date_of_birth = models.DateField()
    place_of_birth = models.TextField(blank=True, null=True)
    civil_status = models.TextField(blank=True, null=True)
    residency = models.TextField(blank=True, null=True)
    origin_country = models.TextField(blank=False, null=False)
    highest_academic_achievement = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    registration_date = models.DateField(blank=False, null=False)
    husband_surname = models.TextField(blank=True, null=True)
    husband_job = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    income = models.FloatField(blank=True, null=True)
    fixed_expenditures = models.FloatField(blank=True, null=True)
    operator = models.ForeignKey(Operators, db_column='operator', null=False, default=0, on_delete=models.SET_DEFAULT)
    phone_1 = models.TextField(blank=True, null=True)
    phone_2 = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('mother-view', kwargs={'pk': self.id})

    def get_modify_url(self):
        return reverse('mother-edit', kwargs={'pk': self.id})

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return format_text(u' '.join([self.name, self.surname]))

    def get_date_of_birth(self):
        return format_date(self.date_of_birth)

    def get_place_of_birth(self):
        return format_text(self.place_of_birth)

    def get_civil_status(self):
        return format_text(self.civil_status)

    def get_residency(self):
        return format_text(self.residency)

    def get_registration_date(self):
        return format_date(self.registration_date)

    def get_origin_country(self):
        return format_text(self.origin_country)

    def get_children(self):
        return Children.objects.filter(mother__exact=self.id)

    def get_num_children(self):
        return len(self.get_children())

    class Meta:
        managed = False
        db_table = 'Mothers'


class Children(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.TextField(blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    sex = models.CharField(blank=True, null=True, max_length=1)
    mother = models.ForeignKey(Mothers, db_column='mother', default=0, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('child-view', kwargs={'pk': self.id})

    def get_modify_url(self):
        return reverse('child-edit', kwargs={'pk': self.id})

    def __str__(self):
        return self.get_name() + ', (' + str(self.get_mother()) + ')'

    def get_name(self):
        return format_text(self.name)

    def get_date_of_birth(self):
        return format_date(self.date_of_birth)

    def get_sex(self):
        return format_text(self.sex)

    def get_mother(self):
        return self.mother

    def is_born(self):
        return self.get_name() != missing()

    class Meta:
        managed = False
        db_table = 'Children'


class Donations(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    date_of_donation = models.DateField(blank=False, null=False)
    requested = models.TextField(blank=True, null=True)
    given = models.TextField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    mother = models.ForeignKey(Mothers, db_column='mother', null=False, default=0, on_delete=models.SET_DEFAULT)
    operator = models.ForeignKey(Operators, db_column='operator', null=False, default=0, on_delete=models.SET_DEFAULT)

    def get_absolute_url(self):
        return reverse('donation-view', kwargs={'pk': self.id})

    def get_modify_url(self):
        return reverse('donation-edit', kwargs={'pk': self.id})

    def __str__(self):
        return self.get_given() + '(' + self.get_date_of_donation() + ')'

    def get_date_of_donation(self):
        return format_date(self.date_of_donation)

    def get_requested(self):
        return format_text(self.requested)

    def get_given(self):
        return format_text(self.given)

    def get_amount(self):
        return self.amount if self.amount is not None else 0.0

    def get_mother(self):
        return self.mother if self.operator else missing()

    def get_operator(self):
        return self.operator if self.operator else missing()

    class Meta:
        managed = False
        db_table = 'Donations'
