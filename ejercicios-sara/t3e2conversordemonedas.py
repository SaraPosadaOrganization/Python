# Función que reciba la cantidad en euros y devuelva el total en dólares (1 euro = 1.1 dólares)
def convertir_a_dolares(euros):
    return euros * 1.1

# Función que reciba la cantidad en euros y devuelva el total en libras (1 euro = 0.87 libras)
def convertir_a_libras(euros):
    return euros * 0.87

# Solicitamos a la usuaria una cantidad en euros
cantidad_en_euros= float(input("Cantidad en euros: "))

# Muestra la cantidad en euros, en dólares y en libras
dolares = convertir_a_dolares(cantidad_en_euros)
libras = convertir_a_libras(cantidad_en_euros)

print(cantidad_en_euros, "euros", dolares, "dolares")
print(cantidad_en_euros, "euros", libras, "libras")
