#from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse ("<h1>Bienvenidos al maravilloso mundo django</h1>")