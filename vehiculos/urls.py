from django.urls import path
from vehiculos import views

urlpatterns = [
    path('autos/', views.AutosLista.as_view() , name= 'autos'),
    path('autos/pedir/', views.PedirAuto.as_view() , name= 'PedirAuto'),
]
