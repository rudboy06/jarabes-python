# Proyecto CRUD de Jarabes con Python + Flask + MySQL + Docker + HTML (Frontend básico)

Este proyecto es un sistema básico de gestión de jarabes, que permite **crear, listar, actualizar y eliminar** registros. Está desarrollado con Python (Flask) como backend, MySQL como base de datos y un frontend simple en HTML, JS y Bootstrap.

---

## Estructura del Proyecto

```
jarabes-python/
├── backend/
│   ├── app.py              # Main Flask app
│   ├── db.py               # Conexión MySQL
│   ├── models.py           # Funciones CRUD
│   ├── requirements.txt    # Dependencias
│   ├── .env                # Variables de entorno
│   └── venv/               # Entorno virtual (ignorar en Git)
├── docker/
│   ├── docker-compose.yml  # Orquestación de contenedores
│   └── mysql/
│       └── init.sql        # Script inicial para crear DB y tabla
├── frontend/
│   └── index.html          # Interfaz HTML simple con JS y Bootstrap
```

---

## Requisitos

- Python 3.10+
- Docker y Docker Compose
- Visual Studio Code (opcional pero recomendado)

---

## 🛠Instalación

### 1. Clonar el proyecto
```bash
git clone https://github.com/usuario/jarabes-python.git
cd jarabes-python
```

### 2. Levantar la base de datos con Docker
```bash
cd docker
docker-compose up -d
```

Esto iniciará un contenedor con MySQL y cargará el script `init.sql` que crea la DB `crud_db` y la tabla `jarabes`.

---

### 3. Preparar backend con Flask
```bash
cd ../backend
py -m venv venv          # Crear entorno virtual
venv\Scripts\activate    # Activar entorno (Windows)

pip install -r requirements.txt
```

---

### 4. Archivo `.env`

Crea un archivo `.env` en `backend/` con el siguiente contenido:

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=crud_db
```

---

### 5. Ejecutar el backend

```bash
py app.py
```

El servidor correrá en:  
`http://127.0.0.1:5000/`

---

### 6. Abrir el frontend

Simplemente abre `frontend/index.html` con doble clic o arrastrándolo a tu navegador.  
 O con Live Server si usas VSCode.

---

## Endpoints de la API

| Método | Endpoint            | Descripción                |
|--------|---------------------|----------------------------|
| GET    | `/jarabes`          | Lista todos los jarabes    |
| POST   | `/jarabes`          | Crea un nuevo jarabe       |
| PUT    | `/jarabes/<id>`     | Actualiza un jarabe        |
| DELETE | `/jarabes/<id>`     | Elimina un jarabe por ID   |

---

## Tecnologías usadas

- Python 3.10
- Flask
- Flask-CORS
- MySQL 8
- Docker + Docker Compose
- Bootstrap 5
- HTML + JS (Fetch API)

---

## Empaquetamiento y despliegue

1. **Frontend:** es estático, puedes copiar `index.html` y servirlo desde cualquier servidor (Nginx, Apache, GitHub Pages, etc.)
2. **Backend:** puedes empaquetar el backend en un contenedor Docker si lo deseas, o ejecutar en una instancia Python.
3. **DB:** ya viene contenida y lista vía Docker.

---

## Autor

Desarrollado por Billi Medina Martinez.  
Contacto: billimedinamartinez@yahoo.com.mx

---

## Licencia

MIT License
