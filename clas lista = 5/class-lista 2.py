class Animal:
    def __init__(self, especie, edad, habitat, alimentos):
        self.especie = especie
        self.edad = edad
        self.habitat = habitat
        self.alimentos = alimentos

animal1 = Animal("Perro", 5, "Casa", ["croquetas", "carne", "huesos"])
print(animal1.alimentos)
print(animal1.especie)