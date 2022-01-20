from django.db import models
from django.db.models.signals import pre_save, post_save

from core.utils.constants import Constants
from core.utils.data_convertion import DataConversion


class ExcelFile(models.Model):
    file_name = models.FileField(upload_to='uploads')
    date_created = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File Id{self.id} File name {self.file_name}'


class CsvFile(models.Model):
    file_name = models.FileField(upload_to='uploads')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'File Id{self.id} File name {self.file_name}'


class ViralLoad(models.Model):
    laboratory_id = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=30, blank=True, null=True)
    number_orig_lab = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    health_facility = models.CharField(max_length=100, blank=True, null=True)
    patient_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    capture_date = models.DateField(null=True, blank=True)
    access_date = models.DateField(null=True, blank=True)
    nid = models.CharField(max_length=100, blank=True, null=True)
    viral_load = models.CharField(max_length=100, null=True, blank=True)
    viral_load_qualitative = models.CharField(
        max_length=100, blank=True, null=True)
    synced = models.BooleanField(default=False)
    formatted_nid = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Viral Load'
        verbose_name_plural = 'Viral Loads'

    def __str__(self):
        return self.patient_name


class Patient(models.Model):
    patient_uuid = models.CharField(max_length=500)
    #person_id = models.IntegerField()
    nid = models.CharField(max_length=100, blank=True, null=True)
    patient_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.patient_name


class Encounter(models.Model):
    encounterDatetime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    encounterType_uuid = models.CharField(
        max_length=255, default=Constants().get_uuids().get('encounter_type'))
    location_uuid = models.CharField(
        max_length=255, default=Constants().get_uuids().get('hpt'))
    form_uuid = models.CharField(
        max_length=255, default=Constants().get_uuids().get('form'))
    synced = models.BooleanField(default=False)

    def __str__(self):
        return self.patient.name


class Observation(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE)
    obsDateTime = models.DateTimeField(auto_now_add=True)
    concept = models.CharField(max_length=255)
    value_numeric = models.PositiveIntegerField(null=True, blank=True)
    value_coded = models.PositiveIntegerField(null=True, blank=True)
    value_datetime = models.DateTimeField(null=True, blank=True)
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE)
    location = models.CharField(
        max_length=255, default=Constants().get_uuids().get('hpt'))
    value = models.CharField(max_length=255)
    voided = models.BooleanField(default=False)
    synced = models.BooleanField(default=False)

    def __str__(self):
        return self.id


# def insert_formatted_nid(sender, instance, created, *args, **kwargs):
#     if created:
#         instance.formatted_nid = DataConversion.format_nid(instance.nid)
#         print(instance.formatted_nid)


# post_save.connect(insert_formatted_nid, sender=ViralLoad)
