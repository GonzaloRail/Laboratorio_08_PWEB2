from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer

class ListaTareasView(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class DetalleTareaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
