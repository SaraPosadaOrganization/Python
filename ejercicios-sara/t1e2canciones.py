#Obtener valores introducidos por la usuaria sobre su canción favorita
titulo = input("¿Cual es tu canción favorita? ")
artista = input("¿Qué artista la compuso? ")
album = input("¿A qué album pertenece? ")
ano = int(input("Año de lanzamiento "))
duracion = int(input("Duración en segundos "))
videoclip = input("¿Tiene videoclip? (verdadero/falso): ")

#Muestra la información introducida
print("Tu canción favorita es", titulo)
print("Su compositor es", artista)
print("Está incluída en el album", album)
print("El año de lanzamiento es", ano)
print("Tiene una duración de (segundos)", duracion)
print("Videoclip", videoclip)

#Obtener valores introducidos por la usuaria sobre la canción que menos le guste
titulo = input("¿Cual es la canción que menos te gusta? ")
artista = input("¿Qué artista la compuso? ")
album = input("¿A qué album pertenece? ")
ano = int(input("Año de lanzamiento "))
duracion = int(input("Duración en segundos "))
videoclip = input("¿Tiene videoclip? (verdadero/falso): ")

#Muestra la información introducida
print("La cancion que menos te gusta es", titulo)
print("Compuesta por", artista)
print("Está incluída en el album", album)
print("El año de lanzamiento es", ano)
print("Tiene una duración de (segundos)", duracion)
print("Videoclip", videoclip)