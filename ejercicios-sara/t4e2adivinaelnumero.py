def adivina_numero(numero):
    if numero == 4:
        return "Has ganado :)"
    else:
        return "Has perdido :("

# Pedimos un número a la usuaria
numero_elegido = int(input("Elige un número entre 1 y 10: "))

# Obtenemos el resultado
mensaje = adivina_numero(numero_elegido)

# Mostramos el resultado
print("Número elegido:", numero_elegido)
print("Resultado:", mensaje)