# Con patrón Flyweight
import random

# Flyweight (peso ligero)
class CaracterFlyweight:
    def __init__(self, valor, fuente, tamaño, color):
        # Estado intrínseco - compartido entre instancias
        self.valor = valor
        self.fuente = fuente
        self.tamaño = tamaño
        self.color = color
    
    def renderizar(self, posicion_x, posicion_y):
        # posicion_x y posicion_y son estados extrínsecos (variables)
        return f"Renderizando '{self.valor}' en la posición ({posicion_x}, {posicion_y}) con fuente {self.fuente}, tamaño {self.tamaño}, color {self.color}"

# Fábrica de Flyweights que gestiona el compartimiento
class FabricaCaracteres:
    def __init__(self):
        self.caracteres = {}
    
    def obtener_caracter(self, valor, fuente, tamaño, color):
        # Clave única para identificar cada configuración única de carácter
        clave = (valor, fuente, tamaño, color)
        
        # Si ya existe este carácter, se reutiliza
        if clave not in self.caracteres:
            self.caracteres[clave] = CaracterFlyweight(valor, fuente, tamaño, color)
        
        return self.caracteres[clave]
    
    def obtener_total_caracteres(self):
        return len(self.caracteres)

class EditorTexto:
    def __init__(self):
        self.fabrica = FabricaCaracteres()
        self.caracteres = []  # Lista de tuplas (carácter, posición_x, posición_y)
    
    def agregar_caracter(self, valor, fuente, tamaño, color, posicion_x, posicion_y):
        # Obtener (o crear) un carácter flyweight
        caracter = self.fabrica.obtener_caracter(valor, fuente, tamaño, color)
        
        # Almacenar el carácter y su estado extrínseco (posición)
        self.caracteres.append((caracter, posicion_x, posicion_y))
    
    def dibujar(self):
        for caracter, posicion_x, posicion_y in self.caracteres:
            print(caracter.renderizar(posicion_x, posicion_y))

# Cliente
def demo_editor_con_flyweight():
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
        
        # Agregar carácter al editor
        editor.agregar_caracter(valor, fuente, tamaño, color, i % 80, i // 80)
    
    # Ahora, en lugar de 100 objetos Caracter, tenemos muchos menos
    # ya que muchos caracteres comparten la misma configuración
    total_objetos = editor.fabrica.obtener_total_caracteres()
    print(f"Usando {total_objetos} objetos Flyweight para {len(editor.caracteres)} caracteres")
    
    # Mostrar solo los primeros 5 caracteres para brevedad
    for i in range(min(5, len(editor.caracteres))):
        caracter, posicion_x, posicion_y = editor.caracteres[i]
        print(caracter.renderizar(posicion_x, posicion_y))

# Ejecutar demostración
demo_editor_con_flyweight()