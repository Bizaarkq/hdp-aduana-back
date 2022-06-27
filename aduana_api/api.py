from cmath import e
from operator import ge
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone

@api_view(['GET'])
def aduana_api_view(request):
    if request.method == 'GET':
        aduanas = Aduana.objects.filter(deleted_at__isnull=True)
        print(aduanas)
        serializer = AduanaSerializer(aduanas, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def archivo_api_view(request):
    if request.method == 'GET':
        archivos = Archivo.objects.filter(deleted_at__isnull=True)
        serializer = ArchivoSerializer(archivos, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def archivo_api_detail_view(request, registro = None):
    archivo = Archivo.objects.filter(numero_registro = registro).first()
    if request.method == 'GET':
        serializer = ArchivoDetailSerializer(archivo)
        return Response(serializer.data, status=200)
    
    #actualizar campos
    elif request.method == 'PUT':
        if 'id_cliente' in request.data:
            if request.data['id_cliente']:
                cliente_db = Cliente.objects.filter(id_cliente = request.data.get('id_cliente', {}).get('id_cliente')).first()
                cliente = ClienteSerializer(cliente_db, data=request.data['id_cliente'])
                if cliente.is_valid():
                    cliente.save()
                else:
                    return Response({'message': 'no se pudo actualizar el transportista'}, status=400)
            elif request.data['id_transporte']:
                transporte_db = Transporte.objects.filter(id_transporte = request.data.get('id_transport', {}).get('id_transporte')).first()
                transporte = TransporteSerializer(transporte_db, data=request.data['id_transporte'])
                if transporte.is_valid():
                    transporte.save()
                else:
                    return Response({'message': 'no se pudo actualizar el transporte'}, status=400)
            elif request.data['id_carga']:
                carga_db = Carga.objects.filter(id_carga = request.data.get('id_carga', {}).get('id_carga')).first()
                carga = CargaSerializer(carga_db, data=request.data['id_carga'])
                if carga.is_valid():
                    carga.save()
                else:
                    return Response({'message': 'no se pudo actualizar la carga'}, status=400)
            elif request.data['id_aduana']:
                aduana = ArchivoSerializer(archivo, data=request.data.get('id_aduana', {}).get('id_aduana'))
                if aduana.is_valid():
                    aduana.save()
                else:
                    return Response({'message': 'no se pudo actualizar la aduana'}, status=400)
            elif request.data['id_municipio']:
                municipio = ArchivoSerializer(archivo, data=request.data.get('id_municipio', {}).get('id_municipio'))
                if municipio.is_valid():
                    municipio.save()
                else:
                    return Response({'message': 'no se pudo actualizar el municipio'}, status=400)
            return Response({'message': 'Archivo creado con exito'}, status=201)
        return Response({'message': 'neles creado con exito'}, status=201)
    #metodo de guardado de archivo
    elif request.method == 'POST':
        
        cliente = ClienteSerializer(data = request.data['id_cliente'])
        if cliente.is_valid():
            cliente_instance = cliente.save()
        else:
            return Response({'message': 'Error en los datos del transportista'}, status=400)

        transporte_data = request.data['id_transporte']
        transporte_data['id_cliente'] = cliente_instance.id_cliente
        transporte = TransporteSerializer(data = transporte_data)
        if transporte.is_valid():
            transporte_instance = transporte.save()
        else:
            return Response({'message': 'Error en los datos del transporte'}, status=400)

        carga_data = request.data['id_carga']
        carga_data['id_transporte'] = transporte_instance.id_transporte
        carga = CargaSerializer(data = carga_data)
        if carga.is_valid():
            carga_instance = carga.save()
        else:
            return Response({'message': 'Error en los datos de la carga'}, status=400)
        
        last_numero_registro = Archivo.objects.last().numero_registro + 1
        print(last_numero_registro)

        serializer = ArchivoSerializer(data={
            'numero_registro': last_numero_registro,
            'id_cliente': cliente_instance.id_cliente,
            'id_aduana': request.data.get('id_aduana', {}).get('id_aduana'),
            'id_transporte': transporte_instance.id_transporte,
            'id_municipio': request.data.get('id_municipio', {}).get('id_municipio'),
            'id_carga': carga_instance.id_carga,
        })
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Archivo creado con exito'}, status=201)
        return Response({'message': 'No se ha creado el archivo, vuelva a intentarlo'}, status=400)
    #eliminar archivo
    elif request.method == 'DELETE':
        archivo.deleted_at = timezone.now()
        archivo.save()
        return Response({'message': 'Archivo eliminado con exito'}, status=200)

@api_view(['POST'])
def aprobacion_api_view(request, registro):
    if request.method == 'POST':
        archivo = Archivo.objects.filter(numero_registro = registro).first()
        archivo.aprobado = True
        archivo.save()
        return Response({'message': 'Archivo aprobado con exito'}, status=200)
    else:
        return Response({'message': 'No se ha podido aprobar el archivo'}, status=400)