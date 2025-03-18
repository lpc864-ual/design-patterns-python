# Con patrón Memento
from datetime import datetime

# Memento (almacena el estado interno del Originador)
class EditorMemento:
    def __init__(self, contenido):
        self._contenido = contenido
        self._fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def obtener_contenido(self):
        return self._contenido
    
    def obtener_fecha(self):
        return self._fecha

# Originador (crea y usa mementos)
class Editor:
    def __init__(self):
        self._contenido = ""
    
    def escribir(self, texto):
        self._contenido += texto
        print(f"Contenido actual: '{self._contenido}'")
    
    def obtener_contenido(self):
        return self._contenido
    
    # Crea un memento con el estado actual
    def guardar(self):
        return EditorMemento(self._contenido)
    
    # Restaura el estado desde un memento
    def restaurar(self, memento):
        self._contenido = memento.obtener_contenido()
        print(f"Contenido restaurado: '{self._contenido}'")

# Cuidador (mantiene una lista de mementos)
class HistorialEditor:
    def __init__(self, editor):
        self._editor = editor
        self._historial = []
        self._indice = -1
    
    def hacer_backup(self):
        print("Guardando estado del editor...")
        self._historial.append(self._editor.guardar())
        self._indice += 1
    
    def deshacer(self):
        if self._indice <= 0:
            print("No hay más acciones para deshacer")
            return
        
        self._indice -= 1
        memento = self._historial[self._indice]
        self._editor.restaurar(memento)
        print(f"Deshacer al estado guardado a las {memento.obtener_fecha()}")
    
    def rehacer(self):
        if self._indice >= len(self._historial) - 1:
            print("No hay más acciones para rehacer")
            return
        
        self._indice += 1
        memento = self._historial[self._indice]
        self._editor.restaurar(memento)
        print(f"Rehacer al estado guardado a las {memento.obtener_fecha()}")
    
    def mostrar_historial(self):
        print("\nHistorial de estados:")
        for i, memento in enumerate(self._historial):
            contenido = memento.obtener_contenido()
            fecha = memento.obtener_fecha()
            marker = " ✓" if i == self._indice else ""
            print(f"{i}: '{contenido}' [{fecha}]{marker}")

# Cliente
editor = Editor()
historial = HistorialEditor(editor)

# Estado inicial vacío
historial.hacer_backup()

editor.escribir("Hola ")
historial.hacer_backup()

editor.escribir("mundo ")
historial.hacer_backup()

editor.escribir("cruel")
historial.hacer_backup()

historial.mostrar_historial()

# Deshacer para volver a "Hola mundo "
print("\nDeshaciendo una vez:")
historial.deshacer()

# Escribir algo nuevo después de deshacer
editor.escribir("hermoso!")
historial.hacer_backup()

historial.mostrar_historial()

# Deshacer todo hasta el principio
print("\nDeshaciendo hasta el principio:")
historial.deshacer()
historial.deshacer()
historial.deshacer()

# Rehacer todo
print("\nRehaciendo todo:")
historial.rehacer()
historial.rehacer()
historial.rehacer()

# Ventajas:
# - Mantiene la encapsulación: solo el Originador puede acceder al estado del Memento
# - Separación clara de responsabilidades
# - Fácil de extender para incluir más estados
# - Simplifica al Originador descargando la responsabilidad de mantener el historial