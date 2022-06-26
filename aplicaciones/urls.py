from django.urls import path
from aplicaciones import views 

urlpatterns = [
    path('',views.iniciar_sesion, name="Iniciar_sesion"),
    path('home',views.home, name="Home"),
    path('gestionar_archivo',views.gestionar_archivo, name="Gestionar_archivo"),
    path('agregar_archivo',views.agregar_archivo, name="Agregar_archivo"),
    path('modificar_archivo',views.modificar_archivo, name="Modificar_archivo"),
    path('control_migratorio',views.control_migratorio, name="Control_migratorio"),
    path('consultar',views.consultar, name="Consultar"),
]
