from rest_framework import serializers
from tecnicas.models import Tecnica,Carrera, MomentoClase, Pensamiento, TipoAgrupacion, Dificultad, Duracion


class TecnicaSerializer(serializers.ModelSerializer):
    carreras = serializers.StringRelatedField(many=True)
    momentos = serializers.StringRelatedField(many=True)
    pensamientos = serializers.StringRelatedField(many=True)
    agrupaciones = serializers.StringRelatedField(many=True)
    dificultades = serializers.StringRelatedField(many=True)
    duraciones = serializers.StringRelatedField(many=True)

    class Meta:
        model = Tecnica
        fields = '__all__'

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ['nombre']

class MomentoClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MomentoClase
        fields = ['nombre']

class PensamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pensamiento
        fields = ['nombre']

class TipoAgrupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAgrupacion
        fields = ['nombre']

class DificultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dificultad
        fields = ['nombre']

class DuracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duracion
        fields = ['nombre']
