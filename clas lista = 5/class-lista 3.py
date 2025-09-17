class Libro:
    def __init__(self, titulo, autor, anio, generos):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.generos = generos

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, ["Realismo mágico", "Novela", "Literatura latinoamericana"])
print(libro1.generos)
print(libro1.titulo)