from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import registros

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request,'formulario.html')

def nuevoUsuario(request):
        #print(request.POST)
        nuevo = registros(nombres=request.POST['nombres'], apellidos=request.POST['apellidos'], postal=request.POST['postal'], correo=request.POST['correo'], usuario=request.POST['usuario'], pais=request.POST['pais'], ciudad=request.POST['ciudad'])
        nuevo.save()
        #return redirect('/formulario/')
        return redirect('index')
        

      
              