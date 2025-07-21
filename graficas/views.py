from django.shortcuts import render
from .models import Registro
from .forms import RegistroForm
from django.shortcuts import redirect

def ver_datos(request):
    registros = Registro.objects.all().order_by('fecha')
    sumatoria = sum(registro.cantidad for registro in registros)
    
    return render(request, 'graficas/ver_datos.html', {
        'registros': registros,
        'sumatoria': sumatoria,
    })


def registrar_datos(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('ver_datos') #render(request, 'graficas/registro_exitoso.html')
    else:
        form = RegistroForm()
    return render(request, 'graficas/registro_form.html', {'form': form})