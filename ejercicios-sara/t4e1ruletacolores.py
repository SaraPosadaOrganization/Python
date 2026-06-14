def mensaje_color(color):
    if color == "rojo":
        return "Pasión y energía."
    elif color == "verde":
        return "Esperanza y crecimiento."
    elif color == "azul":
        return "Calma y serenidad."
    elif color == "amarillo":
        return "Felicidad y optimismo."
    elif color == "morado":
        return "Sabiduría y creatividad."
    else:
        return "Color no válido."
 
 # Pedimos el color a la usuaria
color_elegido = input("Elige un color: ")

# Obtenemos el mensaje
mensaje = mensaje_color(color_elegido)

# Mostramos el resultado
print("Color elegido:", color_elegido)
print("Mensaje:", mensaje)
