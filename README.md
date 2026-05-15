# Nexo-Funkos

Proyecto Django para administrar Funko Pops.

## Estructura del proyecto

- `funkopop/Project/` - código del proyecto Django
  - `Api/` - aplicación principal con modelos, vistas, templates y estáticos
    - `templates/` - plantillas HTML
    - `static/` - CSS, JS y recursos
  - `Project/` - configuración del proyecto (settings, urls, wsgi, asgi)
  - `manage.py` - comando de administración de Django
- `Readme.md` - (anterior) información básica

## Requisitos

- Python 3.8+
- Django (la versión usada originalmente no está fijada; se recomienda crear un virtualenv e instalar Django)

## Instalación local y ejecución

1. Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias (instalar Django si no tienes un `requirements.txt`):

```powershell
pip install django
```

3. Aplicar migraciones y crear superusuario:

```powershell
cd funkopop\Project
python manage.py migrate
python manage.py createsuperuser
```

Sigue los prompts para ingresar usuario y contraseña.

4. Ejecutar el servidor de desarrollo:

```powershell
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/` en el navegador.

## Cuentas de prueba (sugeridas)

Si quieres cuentas de ejemplo, puedes crearlas con el siguiente comando en Django shell:

```powershell
python manage.py shell
```

Y dentro del shell:

```python
from django.contrib.auth.models import User
User.objects.create_superuser('admin','admin@example.com','AdminPass123!')
User.objects.create_user('user','user@example.com','UserPass123!')
exit()
```

- Superusuario: `admin` / `AdminPass123!`
- Usuario normal: `user` / `UserPass123!`

Cambia estas contraseñas en producción.

## Notas

- `db.sqlite3` está ignorada por `.gitignore` (no se sube la base de datos).
- Si necesitas un `requirements.txt`, puedo generarlo inspeccionando el entorno o añadiendo dependencias recomendadas.

## Verificación de archivos subidos

He subido todos los archivos del proyecto fuente (templates, estáticos, código y configuración) a la rama `main` en `https://github.com/LeandroCaballaro/Nexo-Funkos`.

Si quieres, creo un `requirements.txt` y un `CONTRIBUTING.md` ahora.
