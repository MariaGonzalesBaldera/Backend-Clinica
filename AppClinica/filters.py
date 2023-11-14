import django_filters
from .models import Doctor

class DoctorFilterSet(django_filters.FilterSet):
    mode = django_filters.CharFilter(method='filter_mode')

    class Meta:
        model = Doctor
        fields = ['specialty', 'mode']  

    def filter_mode(self, queryset, name, value):
        # Implementa la lógica de filtrado para el campo 'mode' aquí
        return queryset.filter(mode__contains=[value])
