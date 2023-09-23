from django.shortcuts import render

# Create your views here.

def renderizar ( request ):
    return render(request ,'home/prueba.html')
