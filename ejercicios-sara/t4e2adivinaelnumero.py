# Definimos una función para comprobar si el número elegido es ganador o perdedor
def premiado(numero):
    if numero == 4:
        mensaje = "¡Enhorabuena, has acertado!"
    elif numero >= 1 and numero<=10:
        mensaje = "¡Lo sentimos. Has perdido!"
    else:
        mensaje = "úmero incorrecto"
    return mensaje


# Pedimos a la usuaria un número entre 1 y 10
numero_elegido = int(input("Escribe un número del 1 al 10: "))

# Imprimimos el mensaje
mensaje_usuaria = premiado(numero_elegido)
print(mensaje_usuaria)