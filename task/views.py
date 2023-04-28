from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task


# Create your views here.
# aca van todo aquello que responde al cliente
# el crud se puede realizar de forma automatica, no es necesario definir los endpoint
# uno a uno como en express

class TaskView(viewsets.ModelViewSet):
    # importamos la clases ya creadas
    serializer_class = TaskSerializer
    # aca aclaramos que objetos se pueden modificar
    queryset = Task.objects.all()
