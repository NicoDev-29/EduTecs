from django.contrib import admin
from django.contrib.admin import RelatedOnlyFieldListFilter
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields, widgets
from import_export.widgets import ManyToManyWidget
from .models import *

class TecnicaResource(resources.ModelResource):
    carreras = fields.Field(
        column_name='carreras',
        attribute='carreras',
        widget=ManyToManyWidget(Carrera, field='nombre', separator=',')
    )
    momentos = fields.Field(
        column_name='momentos',
        attribute='momentos',
        widget=ManyToManyWidget(MomentoClase, field='nombre', separator=',')
    )
    pensamientos = fields.Field(
        column_name='pensamientos',
        attribute='pensamientos',
        widget=ManyToManyWidget(Pensamiento, field='nombre', separator=',')
    )
    agrupaciones = fields.Field(
        column_name='agrupaciones',
        attribute='agrupaciones',
        widget=ManyToManyWidget(TipoAgrupacion, field='nombre', separator=',')
    )
    dificultades = fields.Field(
        column_name='dificultades',
        attribute='dificultades',
        widget=ManyToManyWidget(Dificultad, field='nombre', separator=',')
    )
    duraciones = fields.Field(
        column_name='duraciones',
        attribute='duraciones',
        widget=ManyToManyWidget(Duracion, field='nombre', separator=',')
    )

    class Meta:
        model = Tecnica
        import_id_fields = ('nombre',)
        fields = ('nombre', 'descripcion', 'explicacion', 'link_externo',
                  'carreras', 'momentos', 'pensamientos', 'agrupaciones',
                  'dificultades', 'duraciones')

    def dehydrate_carreras(self, tecnica):
        return ", ".join([c.nombre for c in tecnica.carreras.all()])

    def dehydrate_momentos(self, tecnica):
        return ", ".join([m.nombre for m in tecnica.momentos.all()])

    def dehydrate_pensamientos(self, tecnica):
        return ", ".join([p.nombre for p in tecnica.pensamientos.all()])

    def dehydrate_agrupaciones(self, tecnica):
        return ", ".join([a.nombre for a in tecnica.agrupaciones.all()])

    def dehydrate_dificultades(self, tecnica):
        return ", ".join([d.nombre for d in tecnica.dificultades.all()])

    def dehydrate_duraciones(self, tecnica):
        return ", ".join([du.nombre for du in tecnica.duraciones.all()])


@admin.register(Tecnica)
class TecnicaAdmin(ImportExportModelAdmin):
    resource_class = TecnicaResource

    list_display = (
        'nombre', 'descripcion', 'explicacion', 'link_externo',
        'carreras_list', 'momentos_list', 'pensamientos_list', 'agrupaciones_list',
        'dificultades_list', 'duraciones_list',
    )

    def carreras_list(self, obj):
        return ", ".join([c.nombre for c in obj.carreras.all()])
    carreras_list.short_description = 'Carreras'

    def momentos_list(self, obj):
        return ", ".join([m.nombre for m in obj.momentos.all()])
    momentos_list.short_description = 'Momentos'

    def pensamientos_list(self, obj):
        return ", ".join([p.nombre for p in obj.pensamientos.all()])
    pensamientos_list.short_description = 'Pensamientos'

    def agrupaciones_list(self, obj):
        return ", ".join([a.nombre for a in obj.agrupaciones.all()])
    agrupaciones_list.short_description = 'Agrupaciones'

    def dificultades_list(self, obj):
        return ", ".join([d.nombre for d in obj.dificultades.all()])
    dificultades_list.short_description = 'Dificultades'

    def duraciones_list(self, obj):
        return ", ".join([du.nombre for du in obj.duraciones.all()])
    duraciones_list.short_description = 'Duraciones'
    
    search_fields = ('nombre', 'descripcion', 'explicacion')

    list_filter = (
        ('pensamientos', RelatedOnlyFieldListFilter),
        ('agrupaciones', RelatedOnlyFieldListFilter),
        ('dificultades', RelatedOnlyFieldListFilter),
        ('duraciones', RelatedOnlyFieldListFilter),
    )

    fieldsets = (
        ("General", {
            "fields": ("nombre", "descripcion", "explicacion", "link_externo")
        }),
        ("Relaciones", {
            "fields": ("carreras", "momentos", "pensamientos", "agrupaciones", "dificultades", "duraciones")
        }),
    )
    jazzmin_section_order = ("general", "relaciones")


@admin.register(Carrera)
class CarreraAdmin(ImportExportModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)



class DificultadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden')
    ordering = ('orden',)

class DuracionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden')
    ordering = ('orden',)

class MomentoClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden')
    ordering = ('orden',)

admin.site.register(MomentoClase, MomentoClaseAdmin)
admin.site.register(Pensamiento)
admin.site.register(TipoAgrupacion)
admin.site.register(Dificultad, DificultadAdmin)
admin.site.register(Duracion, DuracionAdmin)
