#  API - Funko Anime

Proyecto desarrollado con **Django**, orientado a una webpage con  temática de Funkos anime, utilizando estructura MVC de Django, archivos estáticos y plantillas HTML.

---

#  Descripción del Proyecto

El sistema se encuentra organizado utilizando la estructura estándar de Django, separando:

- Lógica de negocio
- Plantillas HTML
- Archivos estáticos
- Configuración del proyecto

---

#  Tecnologías Utilizadas

- Python
- Django
- HTML5
- CSS
- JavaScript
- SQLite3

---

#  Estructura del Proyecto

```bash
Project/
│
├── Api/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   │
│   │   ├── Script/
│   │   │   └── main.js
│   │   │
│   │   └── src/
│   │       ├── dragon.jpg
│   │       ├── iron-throne.jpg
│   │       ├── kings-landing.jpg
│   │       ├── warrior.jpg
│   │       └── winterfell.jpg
│   │
│   ├── templates/
│   │   └── base.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
└── Readme.md
```

---

# Instalación del Proyecto

## 1 Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

---

## 2 Ingresar a la carpeta del proyecto

```bash
cd Project
```

---



## 3 Instalar dependencias

```bash
pip install django
```

---

## 4 Ejecutar migraciones

```bash
python manage.py migrate
```

---

## 5 Ejecutar el servidor

```bash
python manage.py runserver
```

## Datos del Super Usuario
- Usuario: gareis
- Contraseña: 1234


---

# 📄 Licencia

Proyecto de uso educativo y libre para prácticas académicas.