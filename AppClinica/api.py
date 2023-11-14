from rest_framework import viewsets
from .serializer import DoctorSerializer, SpecialtySerializer, DetailDoctorSerializer
from .models import Doctor, Specialty
from django_filters.rest_framework import DjangoFilterBackend
from .filters import DoctorFilterSet

class SpecialtyView(viewsets.ModelViewSet):
  serializer_class = SpecialtySerializer
  queryset = Specialty.objects.all()

class DoctorView(viewsets.ModelViewSet):
  serializer_class = DoctorSerializer
  queryset = Doctor.objects.all()
  filter_backends =[DjangoFilterBackend]
  filterset_fields  = ['specialty','mode']
  filterset_class = DoctorFilterSet

class DetailDoctorView(viewsets.ModelViewSet):
  serializer_class = DetailDoctorSerializer
  queryset = Doctor.objects.get_queryset().order_by('id')
  filter_backends =[DjangoFilterBackend]
  filterset_fields  = ['id']

