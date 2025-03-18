# Con patrón Visitor
import math
from abc import ABC, abstractmethod

# Element interface
class Figura(ABC):
    @abstractmethod
    def aceptar(self, visitor):
        pass

# Concrete Elements
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def aceptar(self, visitor):
        return visitor.visitar_circulo(self)

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def aceptar(self, visitor):
        return visitor.visitar_rectangulo(self)

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def aceptar(self, visitor):
        return visitor.visitar_triangulo(self)

# Visitor interface
class Visitor(ABC):
    @abstractmethod
    def visitar_circulo(self, circulo):
        pass
    
    @abstractmethod
    def visitar_rectangulo(self, rectangulo):
        pass
    
    @abstractmethod
    def visitar_triangulo(self, triangulo):
        pass

# Concrete Visitors
class CalculadorArea(Visitor):
    def visitar_circulo(self, circulo):
        return math.pi * circulo.radio ** 2
    
    def visitar_rectangulo(self, rectangulo):
        return rectangulo.ancho * rectangulo.alto
    
    def visitar_triangulo(self, triangulo):
        return 0.5 * triangulo.base * triangulo.altura

class CalculadorPerimetro(Visitor):
    def visitar_circulo(self, circulo):
        return 2 * math.pi * circulo.radio
    
    def visitar_rectangulo(self, rectangulo):
        return 2 * (rectangulo.ancho + rectangulo.alto)
    
    def visitar_triangulo(self, triangulo):
        return triangulo.lado1 + triangulo.lado2 + triangulo.lado3

class Dibujante(Visitor):
    def visitar_circulo(self, circulo):
        return f"Dibujando un círculo de radio {circulo.radio}"
    
    def visitar_rectangulo(self, rectangulo):
        return f"Dibujando un rectángulo de {rectangulo.ancho}x{rectangulo.alto}"
    
    def visitar_triangulo(self, triangulo):
        return f"Dibujando un triángulo con base {triangulo.base} y altura {triangulo.altura}"

class CalculadorVolumenRevolucion(Visitor):
    def visitar_circulo(self, circulo):
        # Volumen de una esfera
        return (4/3) * math.pi * circulo.radio ** 3
    
    def visitar_rectangulo(self, rectangulo):
        # Volumen al girar alrededor del eje x
        return math.pi * rectangulo.ancho ** 2 * rectangulo.alto
    
    def visitar_triangulo(self, triangulo):
        # Volumen al girar alrededor del eje x (cono)
        return (1/3) * math.pi * (triangulo.base/2) ** 2 * triangulo.altura

# Cliente
figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 4, 3, 4, 5)
]

# Usar los visitantes
calculador_area = CalculadorArea()
calculador_perimetro = CalculadorPerimetro()
dibujante = Dibujante()
calculador_volumen = CalculadorVolumenRevolucion()

print("Áreas:")
for figura in figuras:
    print(f"- {type(figura).__name__}: {figura.aceptar(calculador_area)}")

print("\nPerímetros:")
for figura in figuras:
    print(f"- {type(figura).__name__}: {figura.aceptar(calculador_perimetro)}")

print("\nDibujos:")
for figura in figuras:
    print(f"- {figura.aceptar(dibujante)}")

print("\nVolúmenes de revolución:")
for figura in figuras:
    print(f"- {type(figura).__name__}: {figura.aceptar(calculador_volumen)}")

# Fácil añadir nuevos visitantes sin modificar las clases de figuras
class MedidorComplejidad(Visitor):
    def visitar_circulo(self, circulo):
        return 1  # Complejidad baja
    
    def visitar_rectangulo(self, rectangulo):
        return 2  # Complejidad media
    
    def visitar_triangulo(self, triangulo):
        return 3  # Complejidad alta

medidor = MedidorComplejidad()
print("\nComplejidad de dibujo (1-3):")
for figura in figuras:
    print(f"- {type(figura).__name__}: {figura.aceptar(medidor)}")

# Ventajas:
# - Añadir nuevas operaciones sin modificar las clases existentes
# - Agrupar funcionalidad relacionada en una sola clase visitante
# - Acumular estado mientras se visitan diferentes objetos
# - Separación clara entre algoritmos y objetos sobre los que operan
# - Cumple con el principio Open/Closed