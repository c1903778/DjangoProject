#from django.urls import path
from .views import registro, nuevoUsuario
#
from . import views
from django.urls import path
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.index, name='index'),
    path('formulario/', views.registro, name='formulario'),
    path('formulario/new/', views.nuevoUsuario),
    
]