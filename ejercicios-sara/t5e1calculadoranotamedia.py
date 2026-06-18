def _nota_media(n_notas):
    suma = 0
    # Suma todas las notas mientras las va pidiendo el número de veces indicado
    for i in range (n_notas):
        print("Introduce la nota " +str(i+1))
        suma += float(input())

    # Cuando termina de sumar, calcula la nota media
    nota_media = suma/n_notas
    return nota_media


pregunta = "¿Cuántas notas deseas introducir?"
print (pregunta)
respuesta = int(input())

# Imprime la nota por pantalla
notas = _nota_media(respuesta)
print("La nota media es ", notas)