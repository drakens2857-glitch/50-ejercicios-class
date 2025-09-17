class Nota:
    def __init__(self, contenido):
        self.contenido = contenido

    def guardar(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            archivo.write(self.contenido)


n = Nota("te quedaste sin saldo.")
n = Nota("Recarga hoy.")
n = Nota("Para seguir disfrutando de los beneficios.")
n.guardar("saldo.txt")