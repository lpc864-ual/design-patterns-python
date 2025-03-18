# Sin patrón Memento
class Editor:
    def __init__(self):
        self.contenido = ""
        self.historial_estados = []  # Lista para guardar estados anteriores
        self.posicion_historial = -1
    
    def escribir(self, texto):
        # Guardar estado actual antes de modificar
        self.historial_estados.append(self.contenido)
        self.posicion_historial += 1
        
        # Modificar el contenido
        self.contenido += texto
        print(f"Contenido actual: '{self.contenido}'")
    
    def deshacer(self):
        if self.posicion_historial > 0:
            self.posicion_historial -= 1
            self.contenido = self.historial_estados[self.posicion_historial]
            print(f"Deshacer: '{self.contenido}'")
        else:
            print("No hay más acciones para deshacer")

# Cliente
editor = Editor()
editor.escribir("Hola ")
editor.escribir("mundo")
editor.deshacer()
editor.escribir("amigo")

# Problemas:
# - El estado interno del editor está expuesto (violación de encapsulación)
# - La lógica de respaldo y restauración está mezclada con la lógica de negocio
# - Difícil extender para guardar otros atributos o estados
# - No hay separación clara de responsabilidades