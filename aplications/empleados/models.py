from django.db import models
from aplications.departamento.models import Departamento

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length= 20, unique= True)

    class Meta():
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habiidades Empleados'

    def __str__(self) -> str:
        return f'{self.id} - {self.habilidad}'




class Empleado(models.Model):
    """Modelo para tabla empleado"""
    first_name = models.CharField('Nombre', max_length=60)
    apellidos = models.CharField('Apellidos', max_length=60)

    """Atributo seleccionable"""
    
    job_choices = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
        ('4', 'Secretaria'),
        ('5', 'Servicios Generales'),
        ('6', 'Practicante Universitario'),
        ('7', 'Coordinador'),

    )
    job = models.CharField('Trabajo', max_length= 1, choices= job_choices)

    """"""""""""""""""""""""""""""""""""

    """  Atrubuto que esta relacionado con otra tabla por una foreign key  """

    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    full_name = models.CharField('Nombre completo', max_length= 120, blank = True)

    """"""""""""""""""""""""""""""""""""

    image = models.ImageField('imagen', upload_to= 'empleados/', height_field=None, width_field=None, max_length=None, blank = True)

    ## Relacion de Muchos a Muchos ##

    habilidades = models.ManyToManyField(Habilidades)


    class Meta:
        verbose_name = 'Mi Empleado' 
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['-first_name','apellidos'] 


    def __str__(self) -> str:
        return f'{self.first_name} - {self.apellidos} - {self.job} - {self.image}'
