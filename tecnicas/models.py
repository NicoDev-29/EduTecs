from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        ordering = ['nombre']


class MomentoClase(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    orden = models.PositiveIntegerField(default=0)  
    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['orden']
    
    class Meta:
        verbose_name = "Momento de clase"
        verbose_name_plural = "Momentos de clase"
        ordering = ['nombre']


class Pensamiento(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Pensamiento"
        verbose_name_plural = "Pensamientos"
        ordering = ['nombre']


class TipoAgrupacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Tipo de agrupación"
        verbose_name_plural = "Tipos de agrupación"
        ordering = ['nombre']


class Dificultad(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    orden = models.PositiveIntegerField(default=0)  
    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['orden']
    
    class Meta:
        verbose_name = "Dificultad"
        verbose_name_plural = "Dificultades"
        ordering = ['nombre']


class Duracion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    orden = models.PositiveIntegerField(default=0)  
    
    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['orden']
    
    class Meta:
        verbose_name = "Duración"
        verbose_name_plural = "Duraciones"
        ordering = ['nombre']


class Tecnica(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    explicacion = models.TextField(help_text="Cómo funciona la técnica")
    link_externo = models.URLField(max_length=200, blank=True, null=True, help_text="URL de referencia")
    
    carreras = models.ManyToManyField(Carrera, related_name='tecnicas')
    momentos = models.ManyToManyField(MomentoClase, related_name='tecnicas')
    pensamientos = models.ManyToManyField(Pensamiento, related_name='tecnicas')
    agrupaciones = models.ManyToManyField(TipoAgrupacion, related_name='tecnicas')
    dificultades = models.ManyToManyField(Dificultad, related_name='tecnicas')
    duraciones = models.ManyToManyField(Duracion, related_name='tecnicas')

    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def get_carreras_display(self):
        return self.carreras.all()

    def get_momentos_display(self):
        return self.momentos.all()
    
    def __str__(self):
        return self.nombre


