from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.conf import settings
from aplications.departamento.models import Departamento
from .models import Empleado, Habilidades
from django.shortcuts import (render,get_object_or_404, redirect)
from django.core.mail import send_mail
from .forms import (
    EmpleadoForm,
    RegisterForm,
    getInTouch
)
from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    CreateView
)
# Create your views here.

# class Home_page(TemplateView):
#     """Vista que carga la pagina de inicio"""
#     template_name = 'inicio.html'


class Home_page(ListView):
    model = Departamento
    context_object_name = 'areas'
    template_name = 'inicio.html'

    """Pasar una variable a mi template"""

    
    def get_context_data(self, **kwargs):
        context = super(Home_page, self).get_context_data(**kwargs)

        obj = [
            {
                'title': 'Area Contable',
                'direccion': 'static/img/carrusel1.jpg'
            },
            {
                'title': 'Gerencia',
                'direccion': 'static/img/carrusel2.png'
            },
            {
                'title': 'TI',
                'direccion': 'static/img/carrusel3.jpg'
            },
            {
                'title': 'Otro',
                'direccion': 'static/img/imagen1.jpg'
            },
            {
                'title': 'Area Contable',
                'direccion': 'static/img/imagen2.jpg'
            },
            {
                'title': 'Area Contable',
                'direccion': 'static/img/imagen3.jpg'
            },
        ]

        # Agrega tu formulario al contexto
        context['formulario'] = getInTouch()  # Reemplaza MiFormulario con el nombre de tu formulario

        context['imagenes'] = obj


        return context
    
class listAll(ListView):
    model = Empleado
    template_name = 'empleado/listAll.html'
    context_object_name = 'empleados'
    paginate_by = 6
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agrega un print para ver los datos que se están pasando al contexto
        print(context['empleados'])
        return context
    
    
"""
    Obtenemos el valor de la caja de texto para filtar un empleado

"""

class filterEmploye(ListView):
    template_name = 'empleado/listAll.html'
    context_object_name = 'empleados'
    paginate_by = 4
    def get_queryset(self):
        entrada = self.request.GET.get('kword')
        lista = Empleado.objects.filter(
            first_name__icontains = entrada
        )
        # print(lista)
        return lista
    

class empleadoDetailView(DetailView):
    ## Traemos el empleado ##
    model = Empleado
    template_name = 'empleado/detail.html'
    context_object_name = 'empleado'

    ## Traemos las habilidades
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        skils = Habilidades.objects 
        context['skills'] = Habilidades.objects.filter(empleado=self.object)

        
        return context
    


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/actualizar.html"
    # fields = ['first_name','apellidos','job','departamento','habilidades']
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:list_all')



# class EmpleadoDeleteView(DeleteView):
#     model = Empleado
#     template_name = "empleado/eliminar.html"
#     success_url = reverse_lazy('persona_app:list_all')


def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, id=pk)
    print(f'------------ {empleado}-------{request}')
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('departamento_app:departamentos')
    
    return redirect('persona_app:list_all')  # Redirigir en caso de que la solicitud no sea POST




class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/crear.html"
    form_class = RegisterForm

    success_url = reverse_lazy('persona_app:list_all')
    
    def form_valid(self, form: RegisterForm) -> HttpResponse:
        """
            Aca entra cuando los datos ya estan validos y guardados en la base de datos

        """

        #Logica del proceso
        empleado = form.save(commit= False)
        empleado.full_name = empleado.first_name + ' ' +empleado.apellidos
        empleado.save()

        return super().form_valid(form)


def email( request ):

    if (request.method == 'POST'):

        form = getInTouch(request.POST)
        if form.is_valid():
            # El formulario es válido, haz algo con los datos aquí, por ejemplo, enviar un correo electrónico
            # form.cleaned_data contiene los datos del formulario validados
            # Envía un correo electrónico aquí si es necesario
            # Redirecciona a una página de éxito o muestra un mensaje de éxito.
            datos_formulario = form.cleaned_data
            print(datos_formulario)
            recipient_list = ['nicovalbuena2011@gmail.com']

            send_mail(datos_formulario['subject'], datos_formulario['mensaje'], datos_formulario['email'], recipient_list)

            return redirect('persona_app:home')
        else:
            print(f'Formulario invalido---')
            # Si la solicitud no es un POST, simplemente muestra el formulario en blanco
            form = getInTouch()
    
            return render(request, 'inicio.html', {'form': form})

 

        
        
    
    





    

    

    
    
    
    