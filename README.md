# Proyecto GraphQL API

Este es un proyecto de API GraphQL desarrollado utilizando Django y Graphene. La API permite realizar peticiones GET sobre una base de datos mediante consultas GraphQL.

## Requisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos previos:
- **Python**: Este proyecto requiere Python 3.8 o superior. Verifica tu versión de Python con el comando `python --version`. Puedes descargar la última versión de Python desde el [sitio web oficial de Python](https://www.python.org/downloads/).

## Configuración del entorno

Sigue estos pasos para configurar tu entorno de desarrollo:

1. **Clonar el repositorio**:
    - Si tienes **Git** instalado, abre una terminal y ejecuta el siguiente comando para clonar el repositorio:
      ```bash
      git clone https://github.com/mframosg/GraphQL-API.git
      ```
    - Si **no** tienes Git, puedes descargar el repositorio como un archivo ZIP desde GitHub y descomprimirlo en tu máquina local.

2. **Crear y activar un entorno virtual**:
    - Instala `virtualenv` si aún no lo has hecho:
      ```bash
      pip install virtualenv
      ```
    - Crea un entorno virtual llamado `myenv` (puedes nombrarlo como prefieras) dentro del directorio del proyecto:
      ```bash
      virtualenv myenv
      ```
    - Activa el entorno virtual:
      - En **Windows**:
        ```bash
        myenv\Scripts\activate
        ```
      - En **Unix/MacOS**:
        ```bash
        source myenv/bin/activate
        ```

3. **Instalar dependencias**:
    - Con el entorno virtual activado, instala las dependencias del proyecto ejecutando:
      ```bash
      pip install -r requirements.txt
      ```

4. **Configurar variables de entorno**:
    - Crea un archivo `.env` en el directorio raíz del proyecto para almacenar configuraciones sensibles, como las credenciales de la base de datos:
      ```plaintext
      DATABASE_NAME=nombre_de_tu_base_de_datos
      DATABASE_USER=nombre_de_usuario
      DATABASE_PASSWORD=contraseña
      DATABASE_HOST=dirección_del_host
      DATABASE_PORT=número_de_puerto
      SECRET_KEY=tu_clave_secreta_de_django
      DEBUG=True # o False, en producción
      ```
    - Asegúrate de reemplazar los valores de placeholder con tus configuraciones reales.

## Ejecución del proyecto

Con tu entorno configurado y las dependencias instaladas, estás listo para ejecutar el proyecto:

1. **Migraciones de la base de datos**:
    - Antes de ejecutar el servidor por primera vez, aplica las migraciones de Django para preparar tu base de datos:
      ```bash
      python manage.py migrate
      ```

2. **Ejecutar el servidor de desarrollo**:
    - Inicia el servidor de desarrollo con:
      ```bash
      python manage.py runserver
      ```
    - Navega a `http://localhost:8000/graphql` en tu navegador o utiliza Postman/Insomnia para empezar a realizar consultas GraphQL a tu API.

## Documentación adicional

Esta aplicación es la continuación del primer brackend realizado en django pero basado en una arquitectura REST: https://github.com/mframosg/rest-api

