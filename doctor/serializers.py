from rest_framework import serializers
from .import models

class DoctorSerialize(serializers.ModelSerializer):
    user= serializers.StringRelatedField(many= False)
    designation= serializers.StringRelatedField(many= True)
    specialization= serializers.StringRelatedField(many= True)
    available_time= serializers.StringRelatedField(many= True)
    class Meta:
        model= models.Doctor
        fields= '__all__'

class SpecializationSerialize(serializers.ModelSerializer):
    class Meta:
        model= models.Specialization
        fields= '__all__'

class DesignationSerialize(serializers.ModelSerializer):
    class Meta:
        model= models.Designation
        fields= '__all__'

class AvailableTimeSerialize(serializers.ModelSerializer):
    class Meta:
        model= models.AvailableTime
        fields= '__all__'

class ReviewSerialize(serializers.ModelSerializer):
    class Meta:
        model= models.Review
        fields= '__all__'