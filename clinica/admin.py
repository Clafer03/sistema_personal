from django.contrib import admin
from .models import Cliente, Doctor, Consulta

admin.site.register(Cliente)
admin.site.register(Doctor)
admin.site.register(Consulta)
