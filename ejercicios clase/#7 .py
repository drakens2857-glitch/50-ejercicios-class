class persona:
    def __new__(cls, nombre, edad ):
        print("esto se esta creando" )
        return super(). __new__ (cls)

    def __init__ (self, nombre, edad ):
        print("esto se sigue creando" )
        self.nombre = nombre
        self.edad = edad

    def __del__ (self):
        print("esto se continua creando" )
        ana = persona ("ana", 30 )
        carlos = persona ("carlos", 47 )
        
        print(f' tiene{ana.nombre},años{ana.edad},tiene{carlos.nombre},años{carlos.edad}')
