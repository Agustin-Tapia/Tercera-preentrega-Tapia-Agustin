from django.shortcuts import render
from casa.forms import SillaForm, MesaForm, SillonForm
from casa.models import Silla, Sillon, Mesa
from django.http import HttpResponse
def base(request):
    return render(request, "casa/base.html")

def art_silla(request):

    if request.method == 'POST':
        form = SillaForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            silla = Silla(
                precio_silla = data.get('precio_silla'),
                cantidad_silla = data.get('cantidad_silla')
            )
            silla.save()
            return render(request, 'casa/silla.html', )
        else:
            return render(request, 'casa/silla.html', {'form': form})
        
    form_silla = SillaForm()
    return render(request, 'casa/silla.html', {'form': form_silla})

def buscar_silla(request):

    if request.GET["precio_silla"]: 

        opcion = request.GET.get('precio_silla')
        context = {"sillas":Silla.objects.filter(precio_silla__icontains=opcion).all()} 

    return render(request, 'casa/silla.html', context)

def busquedaSilla (request):
    return render (request, "casa/busqueda.html")


  


def art_sillon(request):

    if request.method == 'POST':
        form = SillonForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            sillon = Sillon(
                precio_sillon = data.get('precio_sillon'),
                cantidad_sillon = data.get('cantidad_sillon')
            )
            sillon.save()
            return render(request, 'casa/sillon.html', )
        else:
            return render(request, 'casa/sillon.html', {'form': form})
        
    form_sillon = SillonForm()
    return render(request, 'casa/sillon.html', {'form': form_sillon})






def art_mesa(request):

    if request.method == 'POST':
        form = MesaForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            mesa = Mesa(
                precio_mesa = data.get('precio_mesa'),
                cantidad_mesa = data.get('cantidad_mesa')
            )
            mesa.save()
            return render(request, 'casa/mesa.html', )
        else:
            return render(request, 'casa/mesa.html', {'form': form})
        
    form_mesa = MesaForm()
    return render(request, 'casa/mesa.html', {'form': form_mesa})



