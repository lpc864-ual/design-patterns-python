# Con patrón Bridge
from abc import ABC, abstractmethod

# Implementación (Color)
class Color(ABC):
    @abstractmethod
    def aplicar(self):
        pass

class ColorRojo(Color):
    def aplicar(self):
        return "rojo"

class ColorAzul(Color):
    def aplicar(self):
        return "azul"

class ColorVerde(Color):
    def aplicar(self):
        return "verde"

# Abstracción (Forma)
class Forma(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def dibujar(self):
        pass

# Refinamientos de la abstracción
class Circulo(Forma):
    def dibujar(self):
        return f"Círculo de color {self.color.aplicar()}"

class Cuadrado(Forma):
    def dibujar(self):
        return f"Cuadrado de color {self.color.aplicar()}"

class Triangulo(Forma):
    def dibujar(self):
        return f"Triángulo de color {self.color.aplicar()}"

# Cliente
# Crear algunas implementaciones de colores
rojo = ColorRojo()
azul = ColorAzul()
verde = ColorVerde()

# Crear algunas abstracciones con implementaciones específicas
circulo = Circulo(rojo)
cuadrado = Cuadrado(azul)
triangulo = Triangulo(verde)

print(circulo.dibujar())
print(cuadrado.dibujar())
print(triangulo.dibujar())

# Fácil de extender con nuevos colores o formas
# Por ejemplo, añadir un nuevo color amarillo:
class ColorAmarillo(Color):
    def aplicar(self):
        return "amarillo"

# Y usarlo con cualquier forma existente
circulo_amarillo = Circulo(ColorAmarillo())
print(circulo_amarillo.dibujar())

# O añadir una nueva forma:
class Rectangulo(Forma):
    def dibujar(self):
        return f"Rectángulo de color {self.color.aplicar()}"

rectangulo_verde = Rectangulo(verde)
print(rectangulo_verde.dibujar())