from django.urls import path
from .views import EquipoListView,Dashboard, EquipoUpdateView, EquipoCreateView, LineaListView,LineaUpdateView,LineaCreateView

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('equipos/', EquipoListView.as_view(), name='equipo_list'),
    path('editequipos/<int:pk>/', EquipoUpdateView.as_view(), name='equipo_edit'),
    path('equipos/nuevo/',EquipoCreateView.as_view(), name='equipo_nuevo'),
    path('lineas/', LineaListView.as_view(), name='linea_list'),
    path('editlineas/<int:pk>/', LineaUpdateView.as_view(), name='linea_edit'),
    path('lineas/nuevo/', LineaCreateView.as_view(),name='linea_nuevo')
]