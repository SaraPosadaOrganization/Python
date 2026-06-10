# Solicitamos datos a la usuaria
nombre = input("Nombre del producto: ")
precio = float(input("Precio por unidad: "))
cantidad = int(input("Cantidad a comprar: "))
descuento = float(input("Descuento (%): "))

# Función que reciba precio, cantidad y descuento y devuelva el precio con descuento aplicado
def calcular_total_descuento(precio, cantidad, descuento):
    total = precio * cantidad
    total_descuento = total * descuento / 100
    return total - total_descuento

# Mostramos cantidad, nombre del producto, descuento y precio total con descuento
precio_final = calcular_total_descuento(precio, cantidad, descuento)
print("Producto:", nombre)
print("Cantidad:", cantidad)
print("Descuento:", descuento, "%")
print("Precio total con descuento:", precio_final, "€")

# Función que reciba una cantidad y le agrege un 21% de IVA
def aplicar_iva(cantidad):
    return cantidad * 1.21

# Mostramos total con IVA aplicado
total_con_iva = aplicar_iva(precio_final)
print("Total con IVA:", total_con_iva, "€")