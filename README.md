# Proyecto GraphQL API

Este es un proyecto de API GraphQL desarrollado utilizando Django y Graphene.

## Requisitos

Para ejecutar este proyecto localmente, necesitarás tener instalado Python en tu máquina. Puedes descargar la última versión de Python desde el [sitio web oficial de Python](https://www.python.org/downloads/).

## Configuración del entorno

1. Clona este repositorio en tu máquina local.
   a. Si tienes instalado Git, puedes clonar el repositorio con el siguiente comando:

      ```bash
        git clone https://github.com/mframosg/.git
        ```
    b. Si no tienes instalado Git, puedes descargar el repositorio como un archivo ZIP y descomprimirlo en tu máquina local.
    c. Una vez que hayas clonado o descargado el repositorio, navega al directorio raíz del proyecto.

2. Crea un entorno virtual para este proyecto. Puedes hacerlo ejecutando el siguiente comando en la terminal:

    a.
        ```bash
        pip install virtualenv
        ```
    b.
        ```bash
        virtualenv myenv
        ```

3. Activa tu entorno virtual. En Windows, puedes hacerlo con el siguiente comando:

    ```bash
    myenv\Scripts\activate
    ```

    En sistemas basados en Unix o MacOS, el comando sería:

    ```bash
    source myenv/bin/activate
    ```

4. Instala las dependencias del proyecto desde el archivo `requirements.txt`. Esto se puede hacer con el siguiente comando:

    ```bash
    pip install -r requirements.txt
    ```

5. Crea un archivo `.env` en el directorio raíz del proyecto y configura las variables de entorno para la base de datos. Por ejemplo:

    ```plaintext
    DATABASE_NAME=maestria
    DATABASE_USER=
    DATABASE_PASSWORD=.
    DATABASE_HOST=
    DATABASE_PORT=
    ```

## Ejecución del proyecto

Una vez que hayas configurado tu entorno, puedes ejecutar el proyecto utilizando el siguiente comando:

```bash
python manage.py runserver
