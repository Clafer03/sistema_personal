from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import ConsultaForm, ClienteForm, DoctorForm
from .models import Consulta

# AGENDAR CONSULTA
# Esta vista maneja el agendamiento de consultas, mostrando un formulario para registrar una nueva
def agendar_consulta(request):
    form = ConsultaForm()
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            try:
                consulta = form.save(commit=False)
                consulta.clean()
                consulta.save()
                messages.success(request, 'Consulta agendada correctamente.')
                return redirect('agendar_consulta')
            except Exception as e:
                messages.error(request, str(e))
    consultas = Consulta.objects.select_related('cliente', 'doctor').order_by('-fecha_hora')
    total_consultas = consultas.count()
    asistidas = consultas.filter(estado_asistencia='asistio').count()
    efectividad = round((asistidas / total_consultas) * 100, 2) if total_consultas > 0 else 0

    return render(request, 'clinica/agendar_consulta.html', {
        'consulta_form': form,
        'consultas': consultas,
        'efectividad': efectividad,
        'asistidas': asistidas,
        'total_consultas': total_consultas,
    })
    
# REGISTRAR CLIENTE Y DOCTOR
# Estas vistas manejan el registro de nuevos clientes y doctores, mostrando formularios para cada uno
def registrar_cliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente registrado correctamente.')
            return redirect('registrar_cliente')
    return render(request, 'clinica/registrar_clientes.html', {'cliente_form': form})

def registrar_doctor(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor registrado correctamente.')
            return redirect('registrar_doctor')
    return render(request, 'clinica/registrar_doctor.html', {'doctor_form': form})

# ACTUALIZAR ASISTENCIA
# Esta vista maneja la actualización del estado de asistencia de una consulta específica
def actualizar_asistencia(request, consulta_id, nuevo_estado):
    consulta = get_object_or_404(Consulta, id=consulta_id)

    if nuevo_estado in ['asistio', 'no_asistio']:
        consulta.estado_asistencia = nuevo_estado
        consulta.save()
        messages.success(request, f"Estado actualizado a: {consulta.get_estado_asistencia_display()}")
    else:
        messages.error(request, "Estado no válido")

    return redirect('agendar_consulta')