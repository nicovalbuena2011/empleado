from typing import Any
from django.db.models.query import QuerySet
from .models import Departamento
from aplications.empleados.models import Empleado
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
    DetailView
)
# Create your views here.



class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/departamentos.html"
    context_object_name = 'departamentos'



class EmpleadoDetailListView(ListView):
    template_name = "departamento/listAll.html"
    context_object_name = 'empleados'
    def get_queryset(self):
        # print(self.kwargs)
        entrada = self.kwargs['dep']
        lista = Empleado.objects.filter(
            departamento__name = entrada
        )
        print(f'{lista}')
        return lista



