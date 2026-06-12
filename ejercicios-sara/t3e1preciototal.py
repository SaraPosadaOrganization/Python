# Función que reciba precio, cantidad y descuento y devuelva el precio con descuento aplicado
def calcular_total_descuento(precio, cantidad, descuento):
    total = precio * cantidad
    total_descuento = total * descuento / 100
    return total - total_descuento

# Función que reciba una cantidad y le agrege un 21% de IVA
def aplicar_iva(precio):
    iva = precio * 0.21
    return precio + iva

# Solicitamos datos a la usuaria
nombre = input("Nombre del producto: ")
precio = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad a comprar: "))
descuento = float(input("Descuento (%): "))

# Mostramos cantidad, nombre del producto, descuento y precio total con descuento
precio_final = calcular_total_descuento(precio, cantidad, descuento)
print("Producto:", nombre)
print("Cantidad:", cantidad)
print("Descuento:", descuento, "%")
print("Precio total con descuento:", precio_final, "€")

# Mostramos total con IVA aplicado
total_con_iva = aplicar_iva(precio_final)
print("Total con IVA:", total_con_iva, "€")
