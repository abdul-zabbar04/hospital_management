from django.contrib import admin
from .models import Appointment
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display= ['patient_name', 'doctor_name', 'appointment_types', 'appointment_status', 'symptom', 'time', 'cancel']
    def patient_name(self, obj):
        return obj.patient.user.first_name
    def doctor_name(self, obj):
        return obj.doctor.user.first_name
    def save_model(self, request, obj, form, change):
        if obj.appointment_status == "Running" and obj.appointment_types == "Online":
            email_subject= "Your appointment is Running."
            email_body= render_to_string('appointment/admin_mail.html', {'patient':obj.patient.user, 'doctor': obj.doctor})
            email= EmailMultiAlternatives(email_subject, '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()

        return super().save_model(request, obj, form, change)
    
admin.site.register(Appointment, AppointmentAdmin)
