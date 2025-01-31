#   ""    SERVIFY     ""

# Aplicacion  de Servicio con Python, Django

## **Documentación Técnica**

### **Introducción del Proyecto**
- **Breve descripción de la aplicación:**
    Esta aplicación permite a los usuarios gestionar servicios de manera eficiente. La plataforma distingue   dos tipos de usuarios:
    *   BUSCADOR: Los usuarios pueden buscar servicios, contratarlos, revisar el estado de sus solicitudes, calificarlos y finalizar servicios en cualquier momento.
    *   OFERENTE: Los usuarios pueden crear servicios, publicar ofertas, aceptar solicitudes, y actualizar el estado de los servicios ofrecidos.

- **Propósito y objetivos del proyecto:**
    El objetivo es proporcionar una plataforma intuitiva, responsiva y accesible para conectar oferentes con buscadores, facilitando la gestión de servicios desde cualquier dispositivo.

### **Guía de Instalación**
- **Requisitos previos**
  - Node.js (versión )
  - python (version )

  entorno virtual 
    python -m venv django-venv
    .\django-venv\Scripts\activate

instalar requerimientos
    pip install -r requirements.txt

ejecutar 
    python3 manage.py runserver

###  **Instrucciones de instalación**
  1. Clona el repositorio:
     ```bash
     git clone https://github.com/TinchoARS/BackServices
     cd backservices
     ```
  2. Activar:
     ```bash
     python -m venv django-venv
    .\django-venv\Scripts\activate
     ```
  3. Aplica las migraciones de base de datos:
     ```bash
     python manage.py migrate
     ```
  4. Instala las dependencias:
     ```bash
     pip install -r requirements.txt
     ```
  5. Inicia la aplicación:
     ```bash
     python3 manage.py runserver
     ```

#### **Descripción de los Módulos**
    Users: Gestión de usuarios, roles y autenticación.
    Services: Creación, publicación y actualización de servicios.
    Interactions: Calificaciones, revisiones y gestión de solicitudes entre buscadores y oferentes.


### **Flujos de trabajo:**

    1. Explorar servicios: Los buscadores pueden navegar por las publicaciones activas.
    2. Contratar servicios: Los buscadores seleccionan y contratan servicios.
    3. Gestión de servicios: Los oferentes pueden administrar las solicitudes y cambiar el estado de sus servicios.

### **Mantenimiento y Actualización:**
#### Convenciones de código:

    pip install --upgrade -r requirements.txt

### **Documentación de Usuario Final**
#### Manual del Usuario:

    1. Abre la aplicación.
    2. codea: python3 manage.py runserver
    3. Accede a la aplicación desde tu navegador en http://127.0.0.1:8000.

### **Configuración del Entorno **
#### Variables de entorno: 
     Crear un archivo .env en la raíz del proyecto con las siguientes variables

    SECRET_KEY= 
    DB_NAME=services
    DB_USER=root
    DB_PASSWORD=root
    DB_HOST=localhost
    DB_PORT=3306


#### Descripción de funcionalidades:
    - Buscar servicios: Permite a los buscadores explorar las ofertas activas.

    - Crear servicios: Permite a los oferentes agregar nuevos servicios a la plataforma.

    - Publicar servicios: Permite a los oferentes crear publicaciones relacionadas con sus servicios.

    - Gestionar solicitudes: Los buscadores pueden revisar el estado de sus servicios contratados y calificarlos.

    - Actualizar estado: Los oferentes pueden cambiar el estado de un servicio según su progreso.

#### Preguntas Frecuentes (FAQs):
    - ¿Cómo contrato un servicio?: Ve a "Publicaciones", selecciona un servicio y haz clic en "Contratar".

    -¿Cómo califico un servicio?: Accede a "Mis solicitudes", selecciona el servicio finalizado y agrega tu calificación.

    -¿Puedo modificar una publicación creada?: Sí, ve a "Publicaciones", selecciona la publicación y edita los detalles.






Proyecto final back-end tematica Servicios.

entorno virtual 
    python -m venv django-venv
    .\django-venv\Scripts\activate

instalar requerimientos
    pip install -r requirements.txt

ejecutar 
    python3 manage.py runserver