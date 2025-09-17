class Curso:
    def __init__(self, nombre, instructor, duracion, temas):
        self.nombre = nombre
        self.instructor = instructor
        self.duracion = duracion
        self.temas = temas

curso1 = Curso("Python Básico", "Juan Pérez", "20 horas", ["Variables", "Listas", "Funciones", "Clases"])
print(curso1.temas)
print(curso1.nombre)