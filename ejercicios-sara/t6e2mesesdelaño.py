# Creamos la lista con los 12 meses
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Pedimos a la usuaria un número del 1 al 12
numero = int(input("Introduce un número del 1 al 12: "))

# Comprobamos si el número es válido
if 1 <= numero <= 12:
    mes_elegido = meses[numero - 1]
    print("El mes es:", mes_elegido)
    
# Si el mes es junio, muestra el mensaje extra
    if mes_elegido == "Junio":
        print("EL MEJOR MES")
else:
    print("Error: El número debe estar entre 1 y 12")
