from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset= models.Appointment.objects.all()
    serializer_class= serializers.AppointmentSerialize

    def get_queryset(self):
        queryset= super().get_queryset()
        patient_id= self.request.query_params.get("patient_id")
        if patient_id:
            queryset= queryset.filter(patient_id= patient_id)
            # This above filter argument: 1st "patient id" is the Appointment model field "patient" which is connected the Patient model by foreign key.Similarly we can get 'doctor_id' for 'doctor' field and 'time_id' for 'time' field of the Appointment model.
        # print(queryset)
        return queryset