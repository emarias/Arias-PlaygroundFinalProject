from django.urls import path
from pagina_empresa.views import inicio, crear_empleado,empleados, ver_empleado, eliminar_empleado, editar_empleado, about

urlpatterns = [
    path('', inicio, name='inicio'),
    path('empleados/nuevo/', crear_empleado, name='crear_empleado'),
    path('empleados/', empleados, name='empleados'),
    path('empleados/<int:id_empleado>/', ver_empleado, name='ver_empleado'),
    path('empleados/<int:id_empleado>/eliminar/', eliminar_empleado, name='eliminar_empleado'),
    path('empleados/<int:id_empleado>/editar/', editar_empleado, name='editar_empleado'),
    path('acercaDeMi/', about, name='acerca_de_mi'),
]
