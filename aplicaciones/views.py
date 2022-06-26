from django.shortcuts import render, HttpResponse

def home (request):
    return render(request, "plantillas/home.html")

def iniciar_sesion (request):
   return render(request, "plantillas/Iniciar_Sesion.html")

def gestionar_archivo(request):
    return render(request, "plantillas/gestionar_archivo.html")

def agregar_archivo (request):
    return render(request, "plantillas/agregar_archivo.html")

def modificar_archivo(request):
    return render(request, "plantillas/modificar_archivo.html")

def control_migratorio(request):
    return render(request, "plantillas/control_migratorio.html")

def consultar(request):
    return render(request, "plantillas/Consultar.html")