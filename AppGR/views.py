from django.shortcuts import render
from django.http import HttpResponse
from AppGR.models import Sombras, Base, Brochas
from django.template import loader
from AppGR.forms import SombrasForm, BaseForm, BrochasForm
# Create your views here.

def inicio(request):

      return render(request, "inicio.html")


def sombras(request):
      sombras = Sombras.objects.all()
      return render(request, "sombras.html", {'sombras': sombras})


def base(request):
      base = Base.objects.all()
      return render(request, "base.html", {'base': base})


def brochas(request):
      brochas = Brochas.objects.all()
      return render(request, "brochas.html", {'brochas': brochas})


def sombras_formulario(request):
      if request.method == 'POST':
            formulario= SombrasForm(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  sombras = Sombras(codigo=data['codigo'], color=data['color'], tipo=data['tipo']  )
                  sombras.save()
                  return render(request, "inicio.html", {"exitoso": True})
      else:  
            formulario= SombrasForm()  
      return render(request, "form_sombras.html", {"formulario": formulario})



def busqueda_sombras(request):
      return render(request, "form_busqueda_sombras.html")



def buscar_sombras(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            sombras = Sombras.objects.filter(codigo__icontains=codigo)
            return render(request, "sombras.html", {'sombras': sombras})
      else:
            return render(request, "sombras.html", {'sombras': []})

def base_formulario(request):
      if request.method == 'POST':
            formulario1= BaseForm(request.POST)

            if formulario1.is_valid():
                  data = formulario1.cleaned_data
                  base = Base(codigo=data['codigo'], tono=data['tono'], cobertura=data['cobertura']  )
                  base.save()
                  return render(request, "inicio.html", {"exitoso": True})
      else:  
            formulario1= BaseForm() 
      return render(request, "form_base.html", {"formulario": formulario1})

def busqueda_base(request):
            return render(request, "form_busqueda_base.html")

def buscar_base(request):
      if request.GET["codigo"]:
            codigo = request.GET["codigo"]
            base = Base.objects.filter(codigo__icontains=codigo)
            return render(request, "base.html", {'base': base})
      else:
            return render(request, "base.html", {'base': []})

def brochas_formulario(request):
      if request.method == 'POST':
            formulario2= BrochasForm(request.POST)

            if formulario2.is_valid():
                  data = formulario2.cleaned_data
                  brochas = Brochas(numero=data['numero'], clase=data['clase'] )
                  brochas.save()
                  return render(request, "inicio.html", {"exitoso": True})
      else:  
            formulario2= BrochasForm()  
      return render(request, "form_brochas.html", {"formulario": formulario2})

def busqueda_brochas(request):
            return render(request, "form_busqueda_brochas.html")

def buscar_brochas(request):
      if request.GET["numero"]:
            numero = request.GET["numero"]
            brochas = Brochas.objects.filter(numero__icontains=numero)
            return render(request, "brochas.html", {'brochas': brochas})
      else:
            return render(request, "brochas.html", {'brochas': []})