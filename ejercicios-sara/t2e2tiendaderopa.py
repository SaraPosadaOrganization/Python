# Precios
camiseta = 10
sudadera = 20.5
gorra = 5.5

# Cantidades
cant_camiseta = int(input("¿Cuántas camisetas quieres? "))
cant_sudadera = int(input("¿Cuántas sudaderas quieres? "))
cant_gorra = int(input("¿Cuántas gorras quieres? "))

# Total de la compra
total = (cant_camiseta * camiseta) + (cant_sudadera * sudadera) + (cant_gorra * gorra)

# IVA (21%)
iva = total * 0.21

# Total final
total_final = total + iva

# Resultado
print("Total de la compra:", total, "€")
print("IVA (21%):", iva, "€")
print("Total a pagar:", total_final, "€")
