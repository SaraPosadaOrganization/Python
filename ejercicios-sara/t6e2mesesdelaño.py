def obtener_mes(numero):
    # Creamos la lista con los 12 meses
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    # Comprobamos si el número es válido
    if numero >= 1 and numero <= 12:
        mes_elegido = meses[numero - 1]
        mensaje = "El mes es: " + mes_elegido

        # Si el número elegido es 6, mensaje extra
        if mes_elegido == "Junio":
            mensaje = mensaje + "\nEL MEJOR MES"
    else:
        mensaje = "Error: El número debe estar entre 1 y 12"

    return mensaje


# Pedimos a la usuaria un número del 1 al 12
numero = int(input("Introduce un número del 1 al 12: "))

# Llamamos a la función y mostramos el resultado
resultado = obtener_mes(numero)
print(resultado)