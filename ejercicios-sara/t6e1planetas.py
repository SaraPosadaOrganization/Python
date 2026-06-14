# Creamos la lista con los 8 planetas
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

# Pedimos a la usuaria un número del 1 al 8
numero = int(input("Introduce un número del 1 al 8: "))

# Mostramos el planeta
if 1 <= numero <= 8:
    print("El planeta correspondiente es:", planetas[numero - 1])

# Mensaje de error si el número no es válido
else:
    print("Error: El número debe estar entre 1 y 8")