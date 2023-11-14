from rest_framework import serializers
from .models import Doctor, Specialty

class DoctorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doctor
    fields = ['id','name','price','idioms','specialty','years_experience','url_map','photo']

class DetailDoctorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Doctor
    fields = '__all__'
    
class SpecialtySerializer(serializers.ModelSerializer):
  class Meta:
    model = Specialty
    fields = '__all__'
