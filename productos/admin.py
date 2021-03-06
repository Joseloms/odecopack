from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from productos.models import (
    Producto
)


# region Productos

# region Action Productos
def activar_seleccionados(modeladmin, request, queryset):
    queryset.update(activo=True)


activar_seleccionados.short_description = "Activar Seleccionados"


def activar_seleccionados_componentes(modeladmin, request, queryset):
    queryset.update(activo_componentes=True)


activar_seleccionados_componentes.short_description = "Activar en Componentes"


def activar_seleccionados_proyectos(modeladmin, request, queryset):
    queryset.update(activo_proyectos=True)


activar_seleccionados_proyectos.short_description = "Activar en Proyectos"


def activar_seleccionados_catalogo(modeladmin, request, queryset):
    queryset.update(activo_catalogo=True)


activar_seleccionados_catalogo.short_description = "Activar en Catalogo"


def activar_seleccionados_ensamble(modeladmin, request, queryset):
    queryset.update(activo_ensamble=True)


activar_seleccionados_ensamble.short_description = "Activar en Ensamble Bandas"


# endregion

class ProductoAdmin(ImportExportModelAdmin):
    fieldsets = (
        ('Informacion General', {
            'classes': ('form-control',),
            'fields':
                (
                    ('id_cguno', 'referencia'),
                    'fabricante', 'serie',
                    'descripcion_estandar',
                    'descripcion_comercial',
                    ('con_nombre_automatico'),
                    'foto_perfil'
                )
        }),
        ('Caracteristicas Físicas', {
            'classes': ('form-control',),
            'fields':
                (
                    ('categoria_dos_por_categoria', 'tipo_por_categoria'),
                    ('material', 'color'),
                    ('ancho', 'alto'),
                    ('costo', 'margen'),
                    ('longitud', 'diametro'),
                    ('cantidad_empaque', 'cantidad_minima_venta', 'unidad_medida'),

                )
        }),
        ('Visualización', {
            'classes': ('form-control',),
            'fields':
                (
                    'activo',
                    ('activo_componentes', 'activo_proyectos', 'activo_catalogo', 'activo_ensamble'),
                )
        })
    )

    actions = [
        activar_seleccionados,
        activar_seleccionados_componentes,
        activar_seleccionados_proyectos,
        activar_seleccionados_catalogo,
        activar_seleccionados_ensamble
    ]

    def get_queryset(self, request):
        qs = Producto.objects.select_related(
            "margen__proveedor__moneda",
            "unidad_medida",
            "margen__categoria",
        ).all()
        return qs

    list_display = (
        'referencia',
        'descripcion_estandar',
        'unidad_medida',
        'margen',
        'costo',
        'get_moneda',
        'get_cambio_moneda',
        'get_factor_importacion',
        'costo_cop',
        'get_margen',
        'precio_base',
        'activo',
        'activo_ensamble',
        'activo_proyectos',
        'activo_componentes',
        'activo_catalogo',
    )
    search_fields = [
        'referencia',
        'descripcion_estandar',
        'descripcion_comercial',
        'color__nombre',
        'material__nombre',
        'serie__nombre',
        'fabricante__nombre',
        'categoria_dos_por_categoria__categoria_uno__nombre',
        'categoria_dos_por_categoria__categoria_dos__nombre',
        'tipo_por_categoria__tipo__nombre',
    ]
    list_filter = (
        'margen__proveedor', 'margen__categoria', 'activo', 'activo_ensamble', 'activo_proyectos', 'activo_componentes',
        'activo_catalogo')

    list_editable = ['activo', 'activo_ensamble', 'activo_proyectos', 'activo_componentes', 'activo_catalogo', 'margen',
                     'costo']
    raw_id_fields = ('margen',)
    readonly_fields = ("precio_base", "costo_cop", "rentabilidad")

    def get_margen(self, obj):
        if obj.margen:
            return obj.margen.margen_deseado
        else:
            return ""

    get_margen.short_description = 'Mgn.'

    def get_factor_importacion(self, obj):
        if obj.margen:
            return obj.margen.proveedor.factor_importacion
        else:
            return ""

    get_factor_importacion.short_description = 'Fac. Imp'

    def get_cambio_moneda(self, obj):
        if obj.margen:
            return obj.margen.proveedor.moneda.cambio
        else:
            return ""

    get_cambio_moneda.short_description = 'Tasa'

    def get_moneda(self, obj):
        if obj.margen:
            return obj.margen.proveedor.moneda
        else:
            return ""

    get_moneda.short_description = 'Moneda'

    def save_model(self, request, obj, form, change):
        obj.get_nombre_automatico('estandar')
        obj.get_nombre_automatico('comercial')
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()


# endregion
admin.site.register(Producto, ProductoAdmin)
