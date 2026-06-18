def obtener_planeta(numero):
    # Lista de planetas
    planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

    # Comprobamos si el número es válido
    if numero >= 1 and numero <= 8:
        mensaje = "El planeta correspondiente es: " + planetas[numero - 1]
    else:
        mensaje = "Error: El número debe estar entre 1 y 8"

    return mensaje


# Pedimos a la usuaria un número del 1 al 8
numero = int(input("Introduce un número del 1 al 8: "))

# Llamamos a la función y mostramos el resultado
resultado = obtener_planeta(numero)

print(resultado)