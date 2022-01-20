from django.contrib import admin

from core.models import CsvFile, ExcelFile, Patient, ViralLoad, Encounter, Observation


class ViralLoadAdmin(admin.ModelAdmin):
    ordering = ['patient_name']
    list_display = [
        'patient_name', 'nid', 'health_facility', 'viral_load', 'viral_load_qualitative', 'capture_date'
    ]
    list_filter = ('viral_load_qualitative', 'health_facility')


admin.site.register(CsvFile)
admin.site.register(ExcelFile)
admin.site.register(ViralLoad, ViralLoadAdmin)
admin.site.register(Patient)
admin.site.register(Encounter)
admin.site.register(Observation)
