class Pelicula:
    def __init__(self, nombre, director, duracion, actores):
        self.nombre = nombre
        self.director = director
        self.duracion = duracion
        self.actores = actores

pelicula1 = Pelicula("Inception", "Christopher Nolan", 148, ["Leonardo DiCaprio", "Elliot Page", "Tom Hardy"])
print(pelicula1.actores)
print(pelicula1.nombre)