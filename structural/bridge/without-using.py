# Sin patrón Bridge
# Problemas: Explosión de clases, difícil mantenimiento, alta acoplamiento

class CirculoRojo:
    def dibujar(self):
        return "Círculo de color rojo"

class CirculoAzul:
    def dibujar(self):
        return "Círculo de color azul"

class CirculoVerde:
    def dibujar(self):
        return "Círculo de color verde"

class CuadradoRojo:
    def dibujar(self):
        return "Cuadrado de color rojo"

class CuadradoAzul:
    def dibujar(self):
        return "Cuadrado de color azul"

class CuadradoVerde:
    def dibujar(self):
        return "Cuadrado de color verde"

class TrianguloRojo:
    def dibujar(self):
        return "Triángulo de color rojo"

class TrianguloAzul:
    def dibujar(self):
        return "Triángulo de color azul"

class TrianguloVerde:
    def dibujar(self):
        return "Triángulo de color verde"

# Cliente
# Si añadimos un nuevo color o forma, necesitamos muchas clases nuevas
circulo = CirculoRojo()
cuadrado = CuadradoAzul()
triangulo = TrianguloVerde()

print(circulo.dibujar())
print(cuadrado.dibujar())
print(triangulo.dibujar())