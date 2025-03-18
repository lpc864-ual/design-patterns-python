# Con patrón Command
from abc import ABC, abstractmethod

# Receptor (receptor de la acción)
class EditorTexto:
    def __init__(self):
        self.texto = ""
    
    def insertar(self, texto):
        self.texto += texto
        print(f"Texto insertado: '{texto}'")
        print(f"Contenido actual: '{self.texto}'")
    
    def eliminar(self, cantidad):
        if cantidad <= len(self.texto):
            texto_eliminado = self.texto[-cantidad:]
            self.texto = self.texto[:-cantidad]
            return texto_eliminado
        else:
            print("Error: No hay suficiente texto para eliminar")
            return ""

# Comando (interfaz)
class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass
    
    @abstractmethod
    def deshacer(self):
        pass

# Comandos concretos
class ComandoInsertar(Comando):
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto
    
    def ejecutar(self):
        self.editor.insertar(self.texto)
    
    def deshacer(self):
        # Para deshacer una inserción, eliminamos el texto insertado
        self.editor.eliminar(len(self.texto))
        print(f"Deshacer: Inserción de '{self.texto}'")
        print(f"Contenido actual: '{self.editor.texto}'")

class ComandoEliminar(Comando):
    def __init__(self, editor, cantidad):
        self.editor = editor
        self.cantidad = cantidad
        self.texto_eliminado = ""
    
    def ejecutar(self):
        self.texto_eliminado = self.editor.eliminar(self.cantidad)
        print(f"Texto eliminado: '{self.texto_eliminado}'")
        print(f"Contenido actual: '{self.editor.texto}'")
    
    def deshacer(self):
        # Para deshacer una eliminación, reinsertamos el texto eliminado
        self.editor.insertar(self.texto_eliminado)
        print(f"Deshacer: Eliminación de '{self.texto_eliminado}'")

# Invocador (mantiene historial y ejecuta comandos)
class ControladorEditor:
    def __init__(self, editor):
        self.editor = editor
        self.historial = []
        self.deshacer_pila = []
    
    def ejecutar(self, comando):
        comando.ejecutar()
        self.historial.append(comando)
        # Limpiar pila de deshacer después de un nuevo comando
        self.deshacer_pila = []
    
    def deshacer(self):
        if not self.historial:
            print("No hay comandos para deshacer")
            return
        
        comando = self.historial.pop()
        comando.deshacer()
        self.deshacer_pila.append(comando)
    
    def rehacer(self):
        if not self.deshacer_pila:
            print("No hay comandos para rehacer")
            return
        
        comando = self.deshacer_pila.pop()
        comando.ejecutar()
        self.historial.append(comando)
    
    def mostrar_historial(self):
        print("\nHistorial de comandos:")
        for i, comando in enumerate(self.historial):
            if isinstance(comando, ComandoInsertar):
                print(f"{i+1}. Insertar: '{comando.texto}'")
            elif isinstance(comando, ComandoEliminar):
                print(f"{i+1}. Eliminar: {comando.cantidad} caracteres ('{comando.texto_eliminado}')")

# Cliente
editor = EditorTexto()
controlador = ControladorEditor(editor)

# Ahora el cliente interactúa con el editor a través de comandos
controlador.ejecutar(ComandoInsertar(editor, "Hola "))
controlador.ejecutar(ComandoInsertar(editor, "mundo "))
controlador.ejecutar(ComandoInsertar(editor, "cruel"))
controlador.ejecutar(ComandoEliminar(editor, 5))

# Mostrar historial
controlador.mostrar_historial()

# Deshacer la última operación (eliminar)
print("\nDeshaciendo la última operación:")
controlador.deshacer()

# Rehacer la operación deshecha
print("\nRehaciendo la operación:")
controlador.rehacer()

# Deshacer dos operaciones
print("\nDeshaciendo dos operaciones:")
controlador.deshacer()
controlador.deshacer()

# Ventajas:
# - Soporte para deshacer/rehacer
# - Historial de comandos
# - Posibilidad de guardar comandos (persistencia)
# - Desacoplamiento entre el cliente y las operaciones