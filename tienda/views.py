from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Pagina tarea
def tarea(request):
    return render(request,"tarea.html")

# Pagina ejemplo JINJA
def ejemplo(request):
    data={
        'title':'Ejemplo JINJA',
        'clist':['PHP','Java','Django','Python','C++','Perl'],
    }
    return render(request,"ejemplo.html",data)