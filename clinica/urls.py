# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('agendar_consulta/', views.agendar_consulta, name='agendar_consulta'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('registrar_doctor/', views.registrar_doctor, name='registrar_doctor'),
    path('consulta/<int:consulta_id>/estado/<str:nuevo_estado>/', views.actualizar_asistencia, name='actualizar_asistencia'),
]
