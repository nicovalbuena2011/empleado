from django.urls import path
from . import views

app_name = "persona_app"



urlpatterns = [
    path('', views.Home_page.as_view(), name = 'home'),
    path('all/',views.listAll.as_view() ,name='list_all'),
    path('filter-Employe/', views.filterEmploye.as_view(), name = 'filtrar'),
    path('employe/<int:pk>', views.empleadoDetailView.as_view(), name = 'detail'),
    path('edit/<int:pk>/', views.EmpleadoUpdateView.as_view(), name = 'editar'),
    path('delete/<int:pk>', views.eliminar_empleado, name = 'eliminar'),
    path('crear/', views.EmpleadoCreateView.as_view(), name = 'crear'),
    path('email/',views.email, name = 'email')
]