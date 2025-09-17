class Nota:
    def __init__(self, contenido):
        self.contenido = contenido

    def guardar(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            archivo.write(self.contenido)


n = Nota("Recordatorio importante.")
n = Nota("este mensaje va con fines informativos.")
n = Nota("No responder.")
n = Nota("fue inscrito exitosamente a la universidad nacional.")
n = Nota("Lo esperamos el dei 12 a las 8 am.")
n = Nota(".................")
n.guardar("Comunicado.txt")