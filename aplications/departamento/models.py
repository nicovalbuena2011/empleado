from django.db import models

# Create your models here.

class Departamento(models.Model):
    # Campo nombre atributo unique hace que no se puedan agregar registros duplicados
    name = models.CharField('Nombre', max_length=50, unique= True)

    # el blank hace que deje pasar ese valor en blanco pero el resto no
    short_name = models.CharField('Nombre Corto', max_length=20, blank= True)
    active = models.BooleanField('Activo', default= False)


    # CLASE META, PARA PERSONALIZAR COMO SE VE EL MODELO EN EL ADMINISTRADOR DE DJANGO

    
    class Meta:
        verbose_name = 'Mi departamento' 
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name'] # Ordena los registros por el nombre en orden alfabetico.

        """
            unique_together 
            no permite que se registren mas registros que tengan igual la combinancion de name y short_name, 
            los compara con los que estan en la base de datos y si encuentra alguno igual, no lo deja registrar

        """
        unique_together = ('name', 'short_name')

    def __str__(self) -> str:
        # return f'{self.name} - {self.short_name} - {str(self.active)}'
        return f'{self.name}'