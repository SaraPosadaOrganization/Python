# Pedimos a la usuaria cuántas notas desea introducir
def calcular_nota_media():
    total_notas = int(input("¿Cuántas notas deseas introducir?: "))
    
    suma_notas = 0
    
# Solicitamos cada nota
    for i in range(total_notas):
        nota = float(input(f"Introduce la nota {i + 1}: "))

# Suma todas las notas
        suma_notas += nota
    
# Devuleve la nota media
    media = suma_notas / total_notas
    return media

# Imprime la nota por pantalla 
nota_final = calcular_nota_media()
print(f"La nota media es: {nota_final}")