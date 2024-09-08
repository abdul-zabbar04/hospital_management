from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
from . import models
from . import serializers


# Create your views here.

class DoctorPagination(pagination.PageNumberPagination):
        page_size = 1
        page_size_query_param = 'page_size'
        max_page_size = 10000

class DoctorViewset(viewsets.ModelViewSet):
    pagination_class= DoctorPagination
    queryset= models.Doctor.objects.all()
    serializer_class= serializers.DoctorSerialize
    
class SpecializationViewset(viewsets.ModelViewSet):
    queryset= models.Specialization.objects.all()
    serializer_class= serializers.SpecializationSerialize

class DesignationViewset(viewsets.ModelViewSet):
    queryset= models.Designation.objects.all()
    serializer_class= serializers.DesignationSerialize

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
     def filter_queryset(self, request, queryset, view):
          doctor_id= request.query_params.get("doctor_id")
          if doctor_id:
               return queryset.filter(doctor = doctor_id )
          return queryset
          


class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset= models.AvailableTime.objects.all()
    serializer_class= serializers.AvailableTimeSerialize
    filter_backends= [AvailableTimeForSpecificDoctor]
    

class ReviwViewset(viewsets.ModelViewSet):
    queryset= models.Review.objects.all()
    serializer_class= serializers.ReviewSerialize
