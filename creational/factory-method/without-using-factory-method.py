# Sin patrón Factory Method
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = "Coche"
    
    def conducir(self):
        return f"Conduciendo un {self.marca} {self.modelo}"

class Motocicleta:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = "Motocicleta"
    
    def conducir(self):
        return f"Pilotando una {self.marca} {self.modelo}"

# Cliente
tipo_vehiculo = input("¿Qué vehículo deseas? (coche/motocicleta): ")
marca = input("Marca: ")
modelo = input("Modelo: ")

# Código condicional que el cliente debe conocer y mantener
if tipo_vehiculo.lower() == "coche":
    vehiculo = Coche(marca, modelo)
elif tipo_vehiculo.lower() == "motocicleta":
    vehiculo = Motocicleta(marca, modelo)
else:
    raise ValueError("Tipo de vehículo no soportado")

print(vehiculo.conducir())