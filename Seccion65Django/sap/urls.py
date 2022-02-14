from django.contrib import admin
from django.urls import path

from webapp.views import bienvenido
from personas.views import detallePersona, nuevaPersona, editarPersona, eliminarPersona

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='inicio'),
    path('detalle_persona/<int:id>', detallePersona),
    path('nueva_persona', nuevaPersona),
    path('editar_persona/<int:id>', editarPersona),
    path('eliminar_persona/<int:id>', eliminarPersona)
]
