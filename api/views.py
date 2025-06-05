from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from tecnicas.models import Tecnica, Carrera, MomentoClase, Pensamiento, TipoAgrupacion, Dificultad, Duracion
from .serializers import (TecnicaSerializer,
    CarreraSerializer, MomentoClaseSerializer, PensamientoSerializer,
    TipoAgrupacionSerializer, DificultadSerializer, DuracionSerializer
)
from .filters import TecnicaFilter
from rest_framework import filters



class CarreraListAPIView(generics.ListAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class MomentoClaseListAPIView(generics.ListAPIView):
    queryset = MomentoClase.objects.all()
    queryset = MomentoClase.objects.order_by('orden')
    serializer_class = MomentoClaseSerializer

class PensamientoListAPIView(generics.ListAPIView):
    queryset = Pensamiento.objects.all()
    serializer_class = PensamientoSerializer

class TipoAgrupacionListAPIView(generics.ListAPIView):
    queryset = TipoAgrupacion.objects.all()
    serializer_class = TipoAgrupacionSerializer

class DificultadListAPIView(generics.ListAPIView):
    queryset = Dificultad.objects.all()
    queryset = Dificultad.objects.order_by('orden')
    serializer_class = DificultadSerializer

class DuracionListAPIView(generics.ListAPIView):
    queryset = Duracion.objects.all()
    queryset = Duracion.objects.order_by('orden')
    serializer_class = DuracionSerializer


class TecnicaListAPIView(generics.ListAPIView):
    queryset = Tecnica.objects.all()
    serializer_class = TecnicaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'carreras__nombre': ['exact', 'in'],
        'momentos__nombre': ['exact', 'in'],
        'duraciones__nombre': ['exact', 'in'],
        'agrupaciones__nombre': ['exact', 'in'],
        'pensamientos__nombre': ['exact', 'in'],
        'dificultades__nombre': ['exact', 'in'],
    }
    search_fields = ['nombre']

