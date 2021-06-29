from django.urls import path
from .views import home, gestion, ingresar, listar, modificar, eliminar
from app import views

urlpatterns = [
    path('', home, name="home"),
    path('gestion/', gestion, name="gestion"),
    
    path('ingresar/', ingresar, name="ingresar"),
    path('listar/', listar, name="listar"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
]