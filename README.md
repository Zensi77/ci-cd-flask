# CI/CD Preproduction - Flask

Este repositorio contiene un flujo de trabajo de CI/CD (Integración Continua/Despliegue Continuo) para una aplicación Flask, configurado con GitHub Actions. El objetivo es automatizar pruebas, construcción de imágenes Docker y despliegue en un entorno de preproducción.

## Estructura del Workflow (`CI/CD Preproduction`)

### Triggers
- **Ejecución automática:** Al hacer `push` en la rama `main`.
- **Ejecución manual:** Desde la pestaña `Actions` de GitHub (usando `workflow_dispatch`).

### Variables de Entorno
- `IMAGE_NAME`: Nombre de la imagen Docker (ejemplo: `ci-cd-python`).

### Jobs

#### 1. **Test**
   - **Objetivo:** Ejecutar pruebas automatizadas.
   - **Pasos:**
      - Configura Python 3.13.
      - Instala dependencias del proyecto (`requirements.txt`).
      - Ejecuta los tests con `unittest` (busca tests en la carpeta `tests`).

#### 2. **Build-and-Push**
   - **Dependencia:** Se ejecuta solo si el job `test` es exitoso.
   - **Objetivo:** Construir y subir una imagen Docker a Docker Hub.
   - **Pasos:**
      - Login en Docker Hub usando credenciales almacenadas en [GitHub Secrets](https://docs.github.com/es/actions/security-guides/encrypted-secrets).
      - Construye la imagen Docker con el formato: `<usuario-docker>/<IMAGE_NAME>:latest`.
      - Sube la imagen al registry de Docker Hub.

## Configuración Requerida
1. **Secrets en GitHub:**
   - `DOCKER_HUB_USERNAME`: Nombre de usuario de Docker Hub.
   - `DOCKER_HUB_TOKEN`: Token de acceso de Docker Hub (creado desde [Account Settings](https://hub.docker.com/settings/security)).

2. **Estructura del Proyecto:**
   - Tests en la carpeta `tests`.
   - `Dockerfile` configurado para la aplicación.
   - `requirements.txt` con las dependencias de Python.

## Flujo del Proceso
```mermaid
graph LR
    A[Push en main] --> B(Ejecutar Tests)
    B --> C{Tests exitosos?}
    C -->|Sí| D[Construir y Subir Imagen]
    C -->|No| E[Fin con error]
