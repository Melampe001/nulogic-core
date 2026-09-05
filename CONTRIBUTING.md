# Guía de Contribución - NULOGIC_CORE

Bienvenido a **NULOGIC_CORE**. Como plataforma de nivel enterprise y cumplimiento financiero global, mantenemos los estándares más estrictos de ingeniería, seguridad (OpenSSF / NIST) y gobernanza regulatoria.

## 1. Código de Conducta y Estándares
- Todo código debe cumplir con las normativas de privacidad (GDPR / LFPDPPP).
- Prohibido incluir credenciales, llaves API o secretos en el historial de Git.

## 2. Developer Certificate of Origin (DCO) - Obligatorio
Para cumplir con las auditorías de propiedad intelectual y gobernanza corporativa, todas las contribuciones deben incluir el DCO. 
Debes firmar tus commits añadiendo el flag -s o agregando manualmente la siguiente línea al final del mensaje del commit:

Signed-off-by: Tu Nombre Real <tu.correo@dominio.com>

Los commits que no contengan esta firma no serán aceptados en la rama principal (master).

## 3. Flujo de Trabajo para Pull Requests (PR)
1. Crea una rama descriptiva (eature/nombre-del-modulo o ix/descripcion).
2. Realiza tus cambios asegurando la calidad del código.
3. Ejecuta las pruebas locales (python main.py).
4. Abre un Pull Request hacia la rama master detallando el propósito del cambio y asegurando el cumplimiento de los estándares de OpenSSF.
