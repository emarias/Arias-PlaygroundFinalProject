from django.urls import path
from pagina_empresa.views import inicio, crear_empleado,empleados

urlpatterns = [
    path('', inicio, name='inicio'),
    path('empleados/nuevo/', crear_empleado, name='crear_empleado'),
    path('empleados/', empleados, name='empleados'),
]
