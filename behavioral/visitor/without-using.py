# Sin patrón Visitor
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    # Añadir nueva operación requiere modificar la clase
    def dibujar(self):
        return f"Dibujando un círculo de radio {self.radio}"
    
    def calcular_volumen_revolucion(self):
        # Volumen de una esfera
        return (4/3) * math.pi * self.radio ** 3

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)
    
    # Añadir nueva operación requiere modificar la clase
    def dibujar(self):
        return f"Dibujando un rectángulo de {self.ancho}x{self.alto}"
    
    def calcular_volumen_revolucion(self):
        # Volumen al girar alrededor del eje x (aproximación)
        return math.pi * self.ancho ** 2 * self.alto

class Triangulo:
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        return 0.5 * self.base * self.altura
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    # Añadir nueva operación requiere modificar la clase
    def dibujar(self):
        return f"Dibujando un triángulo con base {self.base} y altura {self.altura}"
    
    def calcular_volumen_revolucion(self):
        # Volumen al girar alrededor del eje x (cono, aproximación)
        return (1/3) * math.pi * (self.base/2) ** 2 * self.altura

# Cliente
figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 4, 3, 4, 5)
]

print("Áreas:")
for figura in figuras:
    print(f"- {type(figura).__name__}: {figura.calcular_area()}")

print("\nPerímetros:")
for figura in figuras:
    print(f"- {type(figura).__name__}: {figura.calcular_perimetro()}")

print("\nDibujos:")
for figura in figuras:
    print(f"- {figura.dibujar()}")

print("\nVolúmenes de revolución:")
for figura in figuras:
    print(f"- {type(figura).__name__}: {figura.calcular_volumen_revolucion()}")

# Problemas:
# - Cada vez que queremos añadir una nueva operación, debemos modificar todas las clases
# - Si las clases forman parte de una biblioteca externa, puede ser imposible modificarlas
# - Difícil agregar operaciones que actúen en múltiples tipos de objetos
# - El código de operaciones está disperso en múltiples clases