from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)



"""
    Editar la manera en la que se ve la tabla desde el
    administrador de django.

"""

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'apellidos',
        'job',
        'departamento',
        'full_name'

    )

    ##
    ## Añade una columna adicional a la tabla con la concatenacion de los nombres.
    def full_name(self, obj):
        return f'{obj.first_name} {obj.apellidos}'
        
    #

    ## Integrar un buscador
    search_fields = ('first_name',)

    ##Integrar filtros
    list_filter = ('job','habilidades')

    ##AÑADE UN FILTRO MUCHOS A MUCHOS CUANDO SE VA A AGREGAR UN EMPLEADO NUEVOS.
    filter_horizontal = ('habilidades',)

## Se le pasa como segundo paramentro al registrarlo para que lo ordene.
admin.site.register(Empleado, EmpleadoAdmin)

