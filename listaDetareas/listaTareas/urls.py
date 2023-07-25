from django.urls import path
from .views import ListaTareasView, DetalleTareaView

urlpatterns = [
    path('tareas/', ListaTareasView.as_view(), name='lista_tareas'),
    path('tareas/<int:pk>/', DetalleTareaView.as_view(), name='detalle_tarea'),
]
