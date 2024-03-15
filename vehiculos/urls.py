from django.urls import path
from vehiculos import views

urlpatterns = [
    path('autos/', views.AutosLista.as_view() , name= 'autos'),
    path('autos/pedir/', views.PedirAuto.as_view() , name= 'PedirAuto'),
    path('autos/<int:pk>/', views.DetallesAuto.as_view() , name= 'DetallesAuto'),
    path('autos/<int:pk>/editar/', views.EditarAuto.as_view() , name= 'EditarAuto'),
    path('autos/<int:pk>/eliminar/', views.SacarAuto.as_view() , name= 'SacarAuto'),
]
