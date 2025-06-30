# Proyecto de API para Gestión de Scripts y Actualización de Base de Datos ETL

Este proyecto proporciona un entorno basado en **Flet** y **FastAPI** para facilitar la ejecución de scripts de Python y la actualización de datos en un flujo ETL.

## Estructura del proyecto

- `flet_app/`: aplicación de Flet que consume la API y permite lanzar los scripts desde una interfaz web.
- `api/`: API creada con FastAPI para listar y ejecutar los scripts disponibles.
- `scripts/`: directorio donde se almacenan los distintos scripts que se desean ejecutar.
- `requirements.txt`: dependencias necesarias para ejecutar la API y la aplicación de Flet.

## Uso básico

1. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecutar la API:
   ```bash
   uvicorn api.main:app --reload
   ```
3. Lanzar la aplicación de Flet:
   ```bash
   python flet_app/main.py
   ```

A medida que se añadan nuevos scripts en el directorio `scripts/`, estos aparecerán en la interfaz de Flet y podrán ejecutarse desde allí.
