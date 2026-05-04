#  Proyecto Web - Colegio San Felipe Neri

##  Descripción
Este proyecto es una página web institucional desarrollada con Python (Flask) y HTML + Bootstrap, que simula el sitio web de un colegio.

Incluye:
- Página principal con diseño institucional
- Navegación por secciones (Inicio, Académico, etc.)
- Accesos rápidos para estudiantes, docentes y acudientes
- Sección de noticias
- Chat básico tipo IA

---

##  Estructura del proyecto

colegio_web/ 
│ 
├── app.py 
├── templates/
│   └── index.html 
└── static/ (opcional)

---

##  Requisitos

Antes de ejecutar el proyecto necesitas:

- Tener instalado Python (3.14)
- Tener acceso a internet (para cargar Bootstrap)

---

##  Cómo ejecutar el proyecto

1. Abrir la terminal (CMD o PowerShell)

2. Ir a la carpeta del proyecto:
cd ruta/de/tu/carpeta/colegio_web

3. Instalar Flask:
pip install flask

4. Ejecutar el programa:
python app.py

5. Abrir en el navegador:
http://127.0.0.1:5000/

---

##  Uso del sistema

- El usuario puede navegar por el menú principal
- Visualizar información institucional
- Acceder a diferentes secciones
- Interactuar con el chat ingresando mensajes

---

##  Funcionamiento del chat

El chat funciona con lógica básica en el servidor:

- Si el usuario escribe "hola" → responde saludo
- Si escribe "horario" → redirige a sección académica
- Otros mensajes → respuesta genérica

---

##  Tecnologías utilizadas

- Python
- Flask
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

---

##  Notas

- Este proyecto es un prototipo (borrador)
- Puede mejorarse con base de datos, login y conexión a IA real

---

## 👨‍💻 Autor

Proyecto desarrollado con fines educativos.
