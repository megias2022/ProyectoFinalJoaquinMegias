from django.shortcuts import render
from mi_primer_app.models import Familiar 

def index(request):
    return render(request, "mi_primer_app/saludar.html")

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "mi_primer_app/familiares.html", {"lista_familiares": lista_familiares})