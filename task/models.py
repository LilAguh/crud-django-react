from django.db import models

# Create your models here.


class Task(models.Model):
    # Chardfield hace referencia a un string de maximo 200 caracteres
    title = models.CharField(max_length=200)
    # Textfield, guarda un texto mas largo, pero no es necesario escribirlo
    description = models.TextField(blank=True)
    # BooleanField, hace referencia a un booleano, por defecto false y cambia cuando la tarea este completada
    done = models.BooleanField(default=False)

    # necesitamos mostrar una data especifica en el panel, no "task data(numero de task)"
    def __str__(self):
        # aca pedimos que nos retorne el titulo
        return self.title
