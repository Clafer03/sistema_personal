# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('agendar/', views.agendar_consulta, name='agendar_consulta'),
    path('consulta/<int:consulta_id>/estado/<str:nuevo_estado>/', views.actualizar_asistencia, name='actualizar_asistencia'),
]
