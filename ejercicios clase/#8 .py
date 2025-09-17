class producto:
    def __format__(self, formato):
        if formato =="precio":
            return str (self)
                
    def __init__(self, precio, producto):
        self.precio = "32000"
        self.producto = "pan"
    def __str__(self):
        return f'{'precio'},{'producto'}'
    def __repr__(self):
        return f'{'self.precio'}{'self.producto'}'
VAR = producto ("32000", "pan")
print(VAR)
print(repr(VAR))
print(format(VAR, "precio"))
    