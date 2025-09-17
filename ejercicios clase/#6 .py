#persona
class Persona:
    def __init__(self, edad, genero, nacionalidad):
        self.edad = "33"
        self.genero = "masculino"
        self.nacionalidad = "europeo"
persona1 = Persona("33", "masculino", "europeo")
print(persona1.edad)

#granja
class granja:
    def __init__(self, hectareas, animales, ubicacion):
        self.hectareas = "130"
        self.animales = "vacas-pollos-cerdos"
        self.ubicacion = "el corzo"
granja1 = granja("130", "vacas-pollos-cerdos", "el corzo")
print(granja1.animales)

#empresa
class empresa:
    def __init__(self, cargos, instalaciones, empleados):
        self.cargos = "jefe-director-empleados"
        self.instalaciones = "oficinas-taller"
        self.empleados = "50 empleados"
empresa1 = empresa("jefe-director-empleado", "oficinas-taller", "50 empleados")
print(empresa1.empleados)

#sena
class sena:
    def __init__(self, aprendices, instructores, aulas):
        self.aprendices = "4000 aprendices"
        self.instructores = "200 instructores"
        self.aulas = "150 aulas"
senasof = sena("4000 aprendices", "200 instructores", "150 aulas")
print(senasof.aprendices)

#alumnos
class alumnos:
    def __init__(self, materias, calificaciones, horarios):
        self.materia = "15"
        self.calificaciones = "1.0-10.0"
        self.horarios = "5 personas"
alumno1 = alumnos("130v", "mclaren", "5 personas")
print(alumno1.horarios)

