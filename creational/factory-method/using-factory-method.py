# Con patrón Factory Method
from abc import ABC, abstractmethod

# Producto
class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass

# Productos concretos
class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = "Coche"
    
    def conducir(self):
        return f"Conduciendo un {self.marca} {self.modelo}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = "Motocicleta"
    
    def conducir(self):
        return f"Pilotando una {self.marca} {self.modelo}"

# Creador
class FabricaVehiculos(ABC):
    @abstractmethod
    def crear_vehiculo(self, marca, modelo):
        pass
    
    def entregar_vehiculo(self, marca, modelo):
        vehiculo = self.crear_vehiculo(marca, modelo)
        return f"Vehiculo entregado: {vehiculo.conducir()}"

# Creadores concretos
class FabricaCoches(FabricaVehiculos):
    def crear_vehiculo(self, marca, modelo):
        return Coche(marca, modelo)

class FabricaMotocicletas(FabricaVehiculos):
    def crear_vehiculo(self, marca, modelo):
        return Motocicleta(marca, modelo)

# Cliente
tipo_vehiculo = input("¿Qué vehículo deseas? (coche/motocicleta): ")
marca = input("Marca: ")
modelo = input("Modelo: ")

# El cliente trabaja con fábricas concretas
if tipo_vehiculo.lower() == "coche":
    fabrica = FabricaCoches()
elif tipo_vehiculo.lower() == "motocicleta":
    fabrica = FabricaMotocicletas()
else:
    raise ValueError("Tipo de vehículo no soportado")

# El cliente usa la interfaz de la fábrica sin preocuparse por la implementación
fabrica.entregar_vehiculo()
print(fabrica.entregar_vehiculo(marca, modelo))