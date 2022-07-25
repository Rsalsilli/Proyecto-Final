from django.shortcuts import render

from Servicios.models import Streamers, Categorias
# Create your views here.

def streamers(request):

    servicios = Streamers.objects.all()
    return render(request,'Servicios/streamers.html', {"servicios": servicios})

def categoria(request, categorias_id):

    categoria= Categorias.objects.get(id=categorias_id)
    servicios =Streamers.objects.filter(categorias=categoria)
    return render(request, "servicios/categorias.html",{'categoria':categoria, "servicios": servicios})