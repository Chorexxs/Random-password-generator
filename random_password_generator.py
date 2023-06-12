# Programa para crear contraseñas aleatorias de un largo determinado

# Para este programa primero se tienen que importar string y random

import string
import random

# Luego se crea una variable con una lista de la librería string

character = list(string.ascii_letters + string.digits + "!@#$%^&*()")

# Ahora se crea una función en donde el usuario decidirá lo largo que quiere que sea su contraseña


def generate_password():
    password_length = int(
        input("¿Qué tan larga quieres que sea tu contraseña? "))

    random.shuffle(character)

    password = []

    for x in range(password_length):
        password.append(random.choice(character))

    random.shuffle(password)

    password = "".join(password)

    print("Tu contraseña es: " + password)

# Aquí se a creado una opción para que el usuario decida si quiere crear una contra seña o no, y con el statement if se ejecuta el programa


while True:
    option = input("¿Quieres crear una contraseña? (Si/No): ")

    if option == "Si":
        generate_password()
    elif option == "No":
        print("Cerrando programa")
        quit()
    else:
        print("Tienes que escribir Si o No")
        quit()
