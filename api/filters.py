# filters.py
import django_filters
from tecnicas.models import Tecnica

class TecnicaFilter(django_filters.FilterSet):
    carrera_nombre = django_filters.CharFilter(field_name='carreras__nombre', lookup_expr='icontains')
    busqueda = django_filters.CharFilter(method='filter_busqueda')

    class Meta:
        model = Tecnica
        fields = ['carrera_nombre']

    def filter_busqueda(self, queryset, name, value):
        return queryset.filter(
            nombre__icontains=value
        )
