
# Proyecto GraphQL API

Este es un proyecto de API GraphQL desarrollado utilizando Django y Graphene. La API permite realizar consultas y mutaciones sobre una base de datos MySQL, para hacer pruebas de volúmenes de datos.

## Requisitos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos previos:
- **Python**: Este proyecto requiere Python 3.8 o superior. Verifica tu versión de Python con el comando `python --version`. Puedes descargar la última versión de Python desde el [sitio web oficial de Python](https://www.python.org/downloads/).
- **MySQL Workbench**: Este proyecto utiliza una base de datos MySQL. Necesitarás MySQL Workbench para gestionar la base de datos, disponible en el [sitio web oficial](https://www.mysql.com/products/workbench/).

## Configuración del Entorno

Sigue estos pasos para configurar tu entorno de desarrollo:

1. **Clonar el Repositorio**:
   - Utiliza Git para clonar este proyecto y navega al directorio clonado:
     ```bash
     git clone https://github.com/mframosg/GraphQL-API.git
     ```
     ```bash
     cd GraphQL-API
     ```
   - Si **NO** tienes Git, descarga el proyecto como ZIP y descomprímelo.

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
     - En Windows:
       ```bash
       myenv\Scripts\activate
       ```
     - En Unix/MacOS:
       ```bash
       source myenv/bin/activate
       ```

3. **Instalar Dependencias**:
   - Instala las dependencias necesarias ejecutando:
     ```bash
     pip install -r requirements.txt
     ```

## Configuración de la Base de Datos MySQL

Para configurar tu base de datos en MySQL Workbench, sigue estos pasos:

1. **Instalar MySQL Workbench** si aún no lo has hecho. [sitio web oficial](https://www.mysql.com/products/workbench/).
   
2. **Conéctate a tu servidor MySQL**: Abre MySQL Workbench y crea una nueva conexión al servidor MySQL donde deseas alojar tu base de datos. Introduce las credenciales de conexión necesarias.

3. **Crear la Base de Datos**:
   - Abre un nuevo query tab y ejecuta el siguiente comando SQL para crear tu base de datos:
     ```sql
     CREATE DATABASE nombre_de_tu_base_de_datos CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
     ```
   - Asegúrate de reemplazar `nombre_de_tu_base_de_datos` con el nombre que deseas para tu base de datos.
   - Ahora seleccionamos nuestra tabla creada:
       ```sql
      USE nombre_de_tu_base_de_datos;
      ```
4. **Crear la Tabla Necesarias**:
   - Ejecuta el siguiente comando SQL para crear la tabla `usuarios` con el formato especificado:
      ```sql
      CREATE TABLE usuarios (
          idusuario INT AUTO_INCREMENT PRIMARY KEY,
          name VARCHAR(100),
          age INT
      );
      ```
  Con esto ya tenemos nuestra tabla creada.

## Configurar variables de entorno en Django

  - **Crear un Archivo `.env`** en el directorio raíz del proyecto con el siguiente contenido:
      ```plaintext
      DATABASE_NAME=nombre_de_tu_base_de_datos
      DATABASE_USER=nombre_de_usuario
      DATABASE_PASSWORD=contraseña
      DATABASE_HOST=dirección_del_host
      DATABASE_PORT=número_de_puerto 
      ```
      Los valores de `DATABASE_USER`, `DATABASE_PASSWORD`, `DATABASE_HOST` y `DATABASE_PORT` son los que configuraste al crear tu conexión en MySQL Workbench.
      Este es un ejemplo de como debería quedar el archivo `.env` si usas MySQL en local y no has cambiado los valores por defecto:
      ```plaintext
      DATABASE_NAME=nombre_de_tu_base_de_datos
      DATABASE_USER=root
      DATABASE_PASSWORD=
      DATABASE_HOST=localhost
      DATABASE_PORT=3306
      ```

## Ejecución del Proyecto

Con tu entorno configurado y las dependencias instaladas, estás listo para ejecutar el proyecto:

1. **Ejecutar el Servidor de Desarrollo**:
   - Ejecuta el proyecto con Django parado en la raíz del proyecto:
     ```bash
     python manage.py runserver
     ```
   - Accede a la interfaz de GraphQL en `http://127.0.0.1:8000/graphql`.

## Uso de la API GraphQL con Postman

Puedes utilizar Postman para realizar consultas y mutaciones en GraphQL:

- **Para llenar la tabla con registros**:
  Utiliza la mutación GraphQL siguiente en Postman, configurando la petición como POST a `http://127.0.0.1:8000/graphql/`:
  ```
  mutation {
    fillTable(numEntries: 1000000) {
      success
    }
  }
  ```

**Advertencia**: Cada vez que uses el endpoint para agregar usuarios, la base de datos ejecutará un **TRUNCATE** a la tabla, eliminando todos los registros existentes antes de agregar los nuevos.

- **Para recuperar usuarios**:
  Realiza una consulta GraphQL en Postman con la petición configurada como POST a `http://127.0.0.1:8000/graphql/`:
  ```
  {
    users {
      name
      age
    }
  }
  ```

## Documentación Adicional

Esta es la segunda parte del proyecto. Puedes hacer pruebas a la misma base de datos pero con una arquitectura REST en el siguiente enlace: [REST-API](https://github.com/mframosg/rest-api).