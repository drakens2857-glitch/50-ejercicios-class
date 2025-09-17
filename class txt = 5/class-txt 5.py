class Libro:
    def __init__(self, titulo, autor, contenido):
        self.titulo = titulo
        self.autor = autor
        self.contenido = contenido

    def guardar_libro(self):
        with open(f"{self.titulo}.txt", "w") as archivo:
            archivo.write(f"Título: {self.titulo}\nAutor: {self.autor}\n\n{self.contenido}")

libro = Libro("El Viaje", "nelson", "Capítulo 1: El inicio del todo...\nCapítulo 2: La continuidad del todo...")
libro.guardar_libro()
