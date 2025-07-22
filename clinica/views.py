from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import ConsultaForm, ClienteForm, DoctorForm
from .models import Consulta

def agendar_consulta(request):
    consulta_form = ConsultaForm()
    cliente_form = ClienteForm()
    doctor_form = DoctorForm()

    if request.method == 'POST':
        if 'submit_consulta' in request.POST:
            consulta_form = ConsultaForm(request.POST)
            if consulta_form.is_valid():
                try:
                    consulta = consulta_form.save(commit=False)
                    consulta.clean()
                    consulta.save()
                    messages.success(request, 'Consulta agendada correctamente.')
                    return redirect('agendar_consulta')
                except Exception as e:
                    messages.error(request, str(e))
            else:
                messages.error(request, 'Formulario de consulta inválido.')

        elif 'submit_cliente' in request.POST:
            cliente_form = ClienteForm(request.POST)
            if cliente_form.is_valid():
                cliente_form.save()
                messages.success(request, 'Cliente registrado correctamente.')
                return redirect('agendar_consulta')

        elif 'submit_doctor' in request.POST:
            doctor_form = DoctorForm(request.POST)
            if doctor_form.is_valid():
                doctor_form.save()
                messages.success(request, 'Doctor registrado correctamente.')
                return redirect('agendar_consulta')

    consultas = Consulta.objects.select_related('cliente', 'doctor').order_by('-fecha_hora')
    
    total_consultas = consultas.count()
    asistidas = consultas.filter(estado_asistencia='asistio').count()
    
    efectividad = 0
    if total_consultas > 0:
        efectividad = round((asistidas / total_consultas) * 100, 2)

    return render(request, 'clinica/agendar_consulta.html', {
        'consulta_form': consulta_form,
        'cliente_form': cliente_form,
        'doctor_form': doctor_form,
        'consultas': consultas,
        'asistidas': asistidas,
        'efectividad': efectividad,
        'total_consultas': total_consultas
    })
    
def actualizar_asistencia(request, consulta_id, nuevo_estado):
    consulta = get_object_or_404(Consulta, id=consulta_id)

    if nuevo_estado in ['asistio', 'no_asistio']:
        consulta.estado_asistencia = nuevo_estado
        consulta.save()
        messages.success(request, f"Estado actualizado a: {consulta.get_estado_asistencia_display()}")
    else:
        messages.error(request, "Estado no válido")

    return redirect('agendar_consulta')