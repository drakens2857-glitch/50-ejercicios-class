class vehiculo:
    def __init__(self, motor, llantas, capacidad):
        self.motor = "130v"
        self.llantas = "mclaren"
        self.capacidad = "5 personas"
carro2 = vehiculo("130v", "mclaren", "5 personas")
print(carro2.motor)