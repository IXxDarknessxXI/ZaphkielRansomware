# Ransomware en Python

Este proyecto es una implementación de un ransomware simple programado en Python. Su propósito es educativo y de aprendizaje, y no debe ser utilizado en sistemas sin el consentimiento expreso de sus propietarios.

## Descripción

Este script encripta archivos en ciertas ubicaciones del sistema del usuario utilizando la librería `cryptography.fernet`. Además, recoge la dirección IP del usuario y el nombre del usuario del sistema, enviando esta información a un webhook de Discord.

**ADVERTENCIA: Este es un proyecto de código educativo y no debe usarse para actividades maliciosas. El uso no autorizado de este código es ilegal.**

## Requisitos

- Python 3.x
- Librerías de Python:
  - `cryptography`
  - `requests`
  - `pynput`

Puedes instalar las dependencias utilizando `pip`:

```bash
pip install cryptography requests pynput

Instalación
Clona este repositorio en tu máquina local:

bash
Copiar
Editar
git clone https://github.com/tu-usuario/nombre-del-repositorio.git
Abre el archivo ransomware.py y configura tu webhook de Discord reemplazando la siguiente línea:

python
Copiar
Editar
webhook = "Ingresa aqui tu webhook de discord."
Ejecuta el script:

bash
Copiar
Editar
python ransomware.py
