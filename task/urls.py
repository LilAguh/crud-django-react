from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from task import views

# en este archivo se crean las rutas, para posteriormente crear los endpoints

# este router toma todas las rutas y genera las url
routers = routers.DefaultRouter()
routers.register(r'task', views.TaskView, 'task')


# las rutas necesitan 2 parametros
# 1 el nombre de la url + api version
# 2 donde provienen las url generadas por django

urlpatterns = [
    path('api/v1/', include(routers.urls)),
    path('docs/', include_docs_urls(title='Tasks API'))
]

# con esto seria suficiente, ya crea las rutas para las peticiones
# GET, PUT, DELETE, POST
