import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template import loader
from administrador.models import Servicio


def uso_plantilla(request):
    now = datetime.datetime.now()
    doc_externo=loader.get_template('index General.html')
    documento=doc_externo.render({'current_date': now})
    return HttpResponse(documento)

def uso_login(request):
    now = datetime.datetime.now()
    archivo_html= open("D:/Windows 10/Documentos/Ciclo2021-II/APP WEB/ProyectosDjango/proyectoG/proyecto/BOOM/login.html")
    templ2=Template(archivo_html.read())
    archivo_html.close()
    documento=templ2.render(Context({'current_date': now}))
    return HttpResponse(documento)

def listarServicios(request):
    objServicios= Servicio.objects.all()
    return render(request, "index General.html",{"servicios":objServicios})
