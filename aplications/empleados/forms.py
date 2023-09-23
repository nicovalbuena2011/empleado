from django import forms

from aplications.departamento.models import Departamento
from .models import Empleado, Habilidades

class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))

    apellidos = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))

    job = forms.ChoiceField(label = 'Trabajo', choices = Empleado.job_choices, widget = forms.Select(attrs = {'class': 'form-control'}))

    departamento = forms.ModelChoiceField(
        queryset=Departamento.objects.all(),
        label='Departamento',
        widget=forms.Select(attrs={'class': 'form-control'}),  # Agrega clases de Bootstrap
    )


    habilidades = forms.ModelMultipleChoiceField(
        queryset=Habilidades.objects.all(),
        label='Habilidades',
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),  # Agrega clases de Bootstrap
    )

    image = forms.ImageField(
        required=False,  # Para permitir dejar el campo vacío
        label='Imagen',
        widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),  # Agrega clases de Bootstrap
    )

    

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = ['first_name','apellidos','job','departamento','habilidades', 'image']


class RegisterForm(forms.ModelForm):

    """Form definition for Empleado."""
    first_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))

    apellidos = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))

    job = forms.ChoiceField(label = 'Trabajo', choices = Empleado.job_choices, widget = forms.Select(attrs = {'class': 'form-control'}))

    departamento = forms.ModelChoiceField(
        queryset=Departamento.objects.all(),
        label='Departamento',
        widget=forms.Select(attrs={'class': 'form-control'}),  # Agrega clases de Bootstrap
    )


    habilidades = forms.ModelMultipleChoiceField(
        queryset=Habilidades.objects.all(),
        label='Habilidades',
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),  # Agrega clases de Bootstrap
    )

    image = forms.ImageField(
        required=False,  # Para permitir dejar el campo vacío
        label='Imagen',
        widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input'}),  # Agrega clases de Bootstrap
    )

    class Meta:
        model = Empleado
        fields = ('__all__')


class getInTouch(forms.Form):

    name = forms.CharField(label="name", required=True,widget = forms.TextInput(attrs = {'class': 'form-control'}))
    subject = forms.CharField(label="subject", required=True,widget = forms.TextInput(attrs = {'class': 'form-control'}))
    email = forms.EmailField(label="Correo", required=True,widget = forms.TextInput(attrs = {'class': 'form-control'}))
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs = {'class': 'form-control form-control-sm custom-textarea'}))


