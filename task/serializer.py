from rest_framework import serializers
from .models import Task

# Se crea el archivo serializer, que convierte la data de los modelos en Json


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        # nos pide el modelo a inportar
        model = Task
        # podemos seleccionar con una tupla los datos que necesitamos
        # por ejemplo ('id', 'title') y asi seleccionamos solo esos datos
        # pero si queremos todos solo escribimos "__all__"
        fields = '__all__'
