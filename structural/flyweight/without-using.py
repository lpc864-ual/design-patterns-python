# Sin patrón Flyweight
import random

class Caracter:
    def __init__(self, valor, fuente, tamaño, color):
        self.valor = valor
        self.fuente = fuente
        self.tamaño = tamaño
        self.color = color
    
    def renderizar(self, posicion_x, posicion_y):
        return f"Renderizando '{self.valor}' en la posición ({posicion_x}, {posicion_y}) con fuente {self.fuente}, tamaño {self.tamaño}, color {self.color}"

class EditorTexto:
    def __init__(self):
        self.caracteres = []
    
    def agregar_caracter(self, caracter, posicion_x, posicion_y):
        self.caracteres.append((caracter, posicion_x, posicion_y))
    
    def dibujar(self):
        for caracter, posicion_x, posicion_y in self.caracteres:
            print(caracter.renderizar(posicion_x, posicion_y))

# Cliente
def demo_editor_sin_flyweight():
    # Este enfoque consume mucha memoria cuando hay muchos caracteres
    editor = EditorTexto()
    
    fuentes = ["Arial", "Times New Roman", "Courier"]
    tamaños = [10, 12, 14]
    colores = ["Negro", "Rojo", "Azul"]
    
    # Crear un documento con 100 caracteres
    for i in range(100):
        valor = chr(random.randint(97, 122))  # Letras a-z
        fuente = random.choice(fuentes)
        tamaño = random.choice(tamaños)
        color = random.choice(colores)
        
        # Cada carácter es un objeto completo que almacena todos los datos
        caracter = Caracter(valor, fuente, tamaño, color)
        editor.agregar_caracter(caracter, i % 80, i // 80)
    
    # En un documento real con miles o millones de caracteres, esto consumiría mucha memoria
    # ya que cada carácter almacena información redundante (fuente, tamaño, color)
    print(f"Creados {len(editor.caracteres)} caracteres, cada uno con su propia configuración")
    
    # Mostrar solo los primeros 5 caracteres para brevedad
    for i in range(min(5, len(editor.caracteres))):
        caracter, posicion_x, posicion_y = editor.caracteres[i]
        print(caracter.renderizar(posicion_x, posicion_y))

# Ejecutar demostración
demo_editor_sin_flyweight()