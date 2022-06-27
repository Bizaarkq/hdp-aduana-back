from django.urls import path
from .api import *

urlpatterns = [
    path('aduana/', aduana_api_view, name='aduana_api_view'),
    path('archivos/', archivo_api_view, name='archivo_api_view'),
    path('archivo', archivo_api_detail_view, name='archivo_api_detail_view'),
    path('archivo/<int:registro>', archivo_api_detail_view, name='archivo_api_detail_view'),
    path('aprobacion/<int:registro>', aprobacion_api_view, name='aprobacion_api_view'),
]
