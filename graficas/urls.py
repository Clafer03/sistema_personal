from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_datos, name='ver_datos'),
    path('registrar/', views.registrar_datos, name='registrar_datos'),
]
