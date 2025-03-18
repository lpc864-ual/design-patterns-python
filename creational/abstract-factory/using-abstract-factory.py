# Con patrón Abstract Factory
from abc import ABC, abstractmethod

# Productos abstractos
class Boton(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class CuadroTexto(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def input(self):
        pass

# Productos concretos - Windows
class BotonWindows(Boton):
    def render(self):
        return "Renderizando un botón estilo Windows"
    
    def click(self):
        return "Clic en botón de Windows"

class CuadroTextoWindows(CuadroTexto):
    def render(self):
        return "Renderizando un cuadro de texto estilo Windows"
    
    def input(self):
        return "Entrada en cuadro de texto de Windows"

# Productos concretos - Mac
class BotonMac(Boton):
    def render(self):
        return "Renderizando un botón estilo Mac"
    
    def click(self):
        return "Clic en botón de Mac"

class CuadroTextoMac(CuadroTexto):
    def render(self):
        return "Renderizando un cuadro de texto estilo Mac"
    
    def input(self):
        return "Entrada en cuadro de texto de Mac"

# Fábrica abstracta
class FabricaUI(ABC):
    @abstractmethod
    def crear_boton(self):
        pass
    
    @abstractmethod
    def crear_cuadro_texto(self):
        pass

# Fábricas concretas
class FabricaUIWindows(FabricaUI):
    def crear_boton(self):
        return BotonWindows()
    
    def crear_cuadro_texto(self):
        return CuadroTextoWindows()

class FabricaUIMac(FabricaUI):
    def crear_boton(self):
        return BotonMac()
    
    def crear_cuadro_texto(self):
        return CuadroTextoMac()

# Cliente
def crear_ui(fabrica):
    boton = fabrica.crear_boton()
    cuadro_texto = fabrica.crear_cuadro_texto()
    return boton, cuadro_texto

# Determinar qué fábrica usar según el sistema operativo
sistema_operativo = input("¿En qué sistema ejecutamos? (windows/mac): ")

if sistema_operativo.lower() == "windows":
    fabrica = FabricaUIWindows()
elif sistema_operativo.lower() == "mac":
    fabrica = FabricaUIMac()
else:
    raise ValueError("Sistema operativo no soportado")

# El cliente usa la interfaz sin preocuparse por las clases concretas
boton, cuadro_texto = crear_ui(fabrica)
print(boton.render())
print(cuadro_texto.render())