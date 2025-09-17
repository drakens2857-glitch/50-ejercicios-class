class rutinas:
    def __init__(self, edad, genero, nacionalidad, hobbies):
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad
        self.hobbies = hobbies

persona1 =rutinas("33", "masculino", "europeo", ["leer", "correr", "viajar"])
print(persona1.hobbies)
print(persona1.edad)