# Sin patrón Abstract Factory
class BotonWindows:
    def render(self):
        return "Renderizando un botón estilo Windows"
    
    def click(self):
        return "Clic en botón de Windows"

class CuadroTextoWindows:
    def render(self):
        return "Renderizando un cuadro de texto estilo Windows"
    
    def input(self):
        return "Entrada en cuadro de texto de Windows"

class BotonMac:
    def render(self):
        return "Renderizando un botón estilo Mac"
    
    def click(self):
        return "Clic en botón de Mac"

class CuadroTextoMac:
    def render(self):
        return "Renderizando un cuadro de texto estilo Mac"
    
    def input(self):
        return "Entrada en cuadro de texto de Mac"

# Cliente
sistema_operativo = input("¿En qué sistema ejecutamos? (windows/mac): ")

# Crear componentes para el sistema operativo elegido
if sistema_operativo.lower() == "windows":
    boton = BotonWindows()
    cuadro_texto = CuadroTextoWindows()
elif sistema_operativo.lower() == "mac":
    boton = BotonMac()
    cuadro_texto = CuadroTextoMac()
else:
    raise ValueError("Sistema operativo no soportado")

# Usar los componentes
print(boton.render())
print(cuadro_texto.render())