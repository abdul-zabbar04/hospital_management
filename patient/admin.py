from django.contrib import admin
from .models import Patient
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display= ['first_name', 'last_name', 'mobile_no', 'image']
    def first_name(self, patient_obj):
        return patient_obj.user.first_name
    def last_name(self, patient_obj):
        return patient_obj.user.last_name
    
admin.site.register(Patient, PatientAdmin)