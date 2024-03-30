# Proyecto GraphQL API

Este es un proyecto de API GraphQL desarrollado utilizando Django y Graphene. La API permite realizar peticiones GET sobre una base de datos mediante consultas GraphQL.

## Requisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos previos:
- **Python**: Este proyecto requiere Python 3.8 o superior. Verifica tu versión de Python con el comando `python --version`. Puedes descargar la última versión de Python desde el [sitio web oficial de Python](https://www.python.org/downloads/).

## Configuración del entorno

Sigue estos pasos para configurar tu entorno de desarrollo:

1. **Clonar el repositorio**:
   - Crea una nueva carpeta para separar el proyecto de la API REST.
   - Si tienes **Git** instalado, abre una terminal y ejecuta el siguiente comando para clonar el repositorio y cambiar al directorio clonado:
     ```bash
     git clone https://github.com/mframosg/GraphQL-API.git
     cd GraphQL-API
     ```
   - Si **no** tienes Git, descarga el repositorio como un archivo ZIP desde GitHub y descomprímelo en tu máquina local. Luego, abre una terminal y navega al directorio del proyecto clonado.

2. **Configurar el entorno virtual**:
   - El entorno virtual fue creado en la guía anterior, así que ahora solo vamos a activarlo (si ya lo tienes activo, omite este paso):
     - En **Windows**:
       ```bash
       myenv\Scripts\activate
       ```
     - En **Unix/MacOS**:
       ```bash
       source myenv/bin/activate
       ```

3. **Copiar y pegar el archivo .env**:
   - Copia el archivo `.env` del proyecto REST anterior y pégalo en el directorio raíz del proyecto GraphQL API. Este archivo contiene configuraciones sensibles como las credenciales de la base de datos. Asegúrate de revisar y actualizar estas configuraciones según sea necesario.

## Documentación adicional

Para obtener más información sobre el proyecto REST anterior y su arquitectura, puedes visitar el siguiente enlace: [REST-API](https://github.com/mframosg/rest-api).

