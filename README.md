# CRUD REACT FRONTEND - DJANGO BACKEND

Proyecto creado con Django REST para crear la API de las tareas y con React para el cliente.

## Scripts necesarios

### `python3 manage.py runserver` Linux

### `python manage.py runserver` Windows

Inicia el servidor del Backend en modo desarrollador

Abrir [http://localhost:8000](http://localhost:8000) en tu navegador

## Rutas de la API

### `/task/api/v1/task/`

**GET** Muestra la lista con las tareas

### `/task/api/v1/task/`

**POST** Crea una nueva tarea

En el cuerpo de el mensaje debe tener el siguiente formato:

"{
"title": "titulo",
"description": "descripcion",
"done": false
}"

El titulo es obligatorio, la descripcion es opcional y done por defecto es falso
