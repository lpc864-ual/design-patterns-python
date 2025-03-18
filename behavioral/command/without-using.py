# Sin patrón Command
class EditorTexto:
    def __init__(self):
        self.texto = ""
    
    def insertar_texto(self, texto):
        self.texto += texto
        print(f"Texto insertado: '{texto}'")
        print(f"Contenido actual: '{self.texto}'")
    
    def eliminar_texto(self, cantidad):
        if cantidad <= len(self.texto):
            texto_eliminado = self.texto[-cantidad:]
            self.texto = self.texto[:-cantidad]
            print(f"Texto eliminado: '{texto_eliminado}'")
            print(f"Contenido actual: '{self.texto}'")
        else:
            print("Error: No hay suficiente texto para eliminar")

# Cliente
editor = EditorTexto()

# El cliente interactúa directamente con el editor
editor.insertar_texto("Hola ")
editor.insertar_texto("mundo")
editor.eliminar_texto(5)

# Problemas:
# - No podemos deshacer operaciones fácilmente
# - Difícil implementar un historial de comandos
# - No podemos guardar comandos para ejecutarlos más tarde
# - El cliente está acoplado a la implementación del editor