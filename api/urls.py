from django.urls import path
from .views import (
    TecnicaListAPIView,
    CarreraListAPIView,
    MomentoClaseListAPIView,
    PensamientoListAPIView,
    TipoAgrupacionListAPIView,
    DificultadListAPIView,
    DuracionListAPIView
)

urlpatterns = [
    path('tecnicas/', TecnicaListAPIView.as_view(), name='tecnica-list'),
    path('carreras/', CarreraListAPIView.as_view(), name='carrera-list'),
    path('momentos/', MomentoClaseListAPIView.as_view(), name='momentoclase-list'),
    path('pensamientos/', PensamientoListAPIView.as_view(), name='pensamiento-list'),
    path('agrupaciones/', TipoAgrupacionListAPIView.as_view(), name='tipoagrupacion-list'),
    path('dificultades/', DificultadListAPIView.as_view(), name='dificultad-list'),
    path('duraciones/', DuracionListAPIView.as_view(), name='duracion-list'),
]
