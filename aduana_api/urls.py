from django.urls import path
from .api import *

urlpatterns = [
    path('aduana', aduana_api_view, name='aduana_api_view'),
    path('departamentos', get_all_departamentos, name='get_all_departamentos'),
    path('municipios/<str:id_departamento>', get_municipios, name='get_municipios'),
    path('archivos/', archivo_api_view, name='archivo_api_view'),
    path('archivo', archivo_api_detail_view, name='archivo_api_detail_view'),
    path('archivo/<int:registro>', archivo_api_detail_view, name='archivo_api_detail_view'),
    path('aprobacion/<int:registro>', aprobacion_api_view, name='aprobacion_api_view'),
    path('user', current_user, name='current_user'),
]
