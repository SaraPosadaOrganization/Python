# Pedir a usuaria 5 veces que introduzca un color
for i in range(5):
    color = input("Introduce un color: ").lower()

    if color == "azul":
        print("¡Premio conseguido!")
        break
    else:
        if i < 4:
            print("Prueba otro color")
       
    
