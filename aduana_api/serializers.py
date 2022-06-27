from rest_framework import serializers
from .models import *

class AduanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aduana
        exclude = ['created_at', 'created_user', 'updated_at', 'updated_user', 'deleted_at']

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        exclude = ['created_at', 'created_user', 'updated_at', 'updated_user', 'deleted_at']

class MunicipioSerializer(serializers.ModelSerializer):
    id_departamento = DepartamentoSerializer()
    class Meta:
        model = Municipio
        exclude = ['created_at', 'created_user', 'updated_at', 'updated_user', 'deleted_at']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ['created_at', 'created_user', 'updated_at', 'updated_user', 'deleted_at']

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        exclude = ['created_at', 'created_user', 'updated_at', 'updated_user', 'deleted_at']

class CargaSerializer(serializers.ModelSerializer):
    #id_transporte = TransporteSerializer()
    class Meta:
        model = Carga
        exclude = ['created_at', 'created_user', 'updated_at', 'updated_user', 'deleted_at']

class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        exclude = ['created_at', 'created_user', 'updated_at', 'updated_user', 'deleted_at']

class ArchivoDetailSerializer(serializers.ModelSerializer):
    id_municipio = MunicipioSerializer()
    id_cliente = ClienteSerializer()
    id_aduana = AduanaSerializer()
    id_transporte = TransporteSerializer()
    id_carga = CargaSerializer()
    class Meta:
        model = Archivo
        exclude = ['created_at', 'created_user', 'updated_at', 'updated_user', 'deleted_at']

class TransportistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportista
        exclude = ['created_at', 'created_user', 'updated_at', 'updated_user', 'deleted_at']