from django.urls import path
from . import views


app_name = "departamento_app"

urlpatterns = [
    path('departments/', views.DepartamentoListView.as_view(), name = 'departamentos'),
    path('detail/<str:dep>/', views.EmpleadoDetailListView.as_view(), name = 'detail_dep')
    
]