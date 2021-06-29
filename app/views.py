from django.shortcuts import render, redirect, get_object_or_404
from .models import Despacho
from .forms import DespachoForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def gestion(request):
    return render(request, 'gestion.html')

def listar(request):
    despachos = Despacho.objects.all()
    data = {
        'despachos': despachos
    }
    return render(request,"listar.html",data)

def ingresar(request):
    data = {
        'form': DespachoForm()
    }
    if request.method == 'POST':
        formulario = DespachoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
            return redirect(to="listar")
        else:
            data["form"] = formulario
    return render(request,"ingresar.html",data)

def eliminar(request, id):
    despacho = get_object_or_404(Despacho, id=id)
    despacho.delete()
    return redirect(to="listar")


def modificar(request, id):
    despacho = get_object_or_404(Despacho, id=id)
    data={
        'form': DespachoForm(instance=despacho)
    }
    if request.method == 'POST':
        formulario = DespachoForm(data=request.POST, instance=despacho)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Editado correctamente"
            return redirect(to="listar")
        data["form"] = formulario

    return render(request,"modificar.html",data)

