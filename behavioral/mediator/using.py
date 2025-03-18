# Con patrón Mediator
from abc import ABC, abstractmethod

# Mediador abstracto
class Mediador(ABC):
    @abstractmethod
    def registrar(self, colega):
        pass
    
    @abstractmethod
    def enviar_mensaje(self, mensaje, remitente, destinatario=None):
        pass

# Colega abstracto
class Colega(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self.mediador = None
    
    def establecer_mediador(self, mediador):
        self.mediador = mediador
    
    @abstractmethod
    def enviar(self, mensaje, destinatario=None):
        pass
    
    @abstractmethod
    def recibir(self, mensaje, remitente):
        pass

# Mediador concreto (Sala de chat)
class SalaChat(Mediador):
    def __init__(self, nombre):
        self.nombre = nombre
        self.colegas = {}
    
    def registrar(self, colega):
        self.colegas[colega.nombre] = colega
        colega.establecer_mediador(self)
    
    def enviar_mensaje(self, mensaje, remitente, destinatario=None):
        if destinatario:
            # Mensaje privado
            if destinatario in self.colegas:
                self.colegas[destinatario].recibir(mensaje, remitente.nombre)
            else:
                print(f"Usuario {destinatario} no encontrado")
        else:
            # Mensaje a todos (excepto al remitente)
            for nombre, colega in self.colegas.items():
                if nombre != remitente.nombre:
                    colega.recibir(mensaje, remitente.nombre)

# Colega concreto
class Usuario(Colega):
    def enviar(self, mensaje, destinatario=None):
        print(f"{self.nombre} envía mensaje" + 
              (f" a {destinatario}" if destinatario else " a todos"))
        self.mediador.enviar_mensaje(mensaje, self, destinatario)
    
    def recibir(self, mensaje, remitente):
        print(f"{self.nombre} recibe mensaje de {remitente}: {mensaje}")

# Cliente
sala_chat = SalaChat("Sala Principal")

# Crear usuarios
alice = Usuario("Alice")
bob = Usuario("Bob")
charlie = Usuario("Charlie")
dave = Usuario("Dave")

# Registrar usuarios en la sala de chat (mediador)
sala_chat.registrar(alice)
sala_chat.registrar(bob)
sala_chat.registrar(charlie)
sala_chat.registrar(dave)

# Enviar mensajes a través del mediador
print("Mensajes privados:")
alice.enviar("Hola Bob", "Bob")
bob.enviar("Hola Alice", "Alice")

print("\nMensajes grupales:")
alice.enviar("Hola a todos")

# Extensiones posibles del patrón Mediator:
class SalaChatAvanzada(SalaChat):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.historial = []
    
    def enviar_mensaje(self, mensaje, remitente, destinatario=None):
        # Registrar en historial
        entrada = {
            "remitente": remitente.nombre,
            "destinatario": destinatario,
            "mensaje": mensaje,
            "tipo": "privado" if destinatario else "grupal"
        }
        self.historial.append(entrada)
        
        # Llamar al método original
        super().enviar_mensaje(mensaje, remitente, destinatario)
    
    def mostrar_historial(self):
        print(f"\nHistorial de mensajes de {self.nombre}:")
        for entrada in self.historial:
            tipo = entrada["tipo"]
            remitente = entrada["remitente"]
            destinatario = entrada["destinatario"]
            mensaje = entrada["mensaje"]
            
            if tipo == "privado":
                print(f"{remitente} a {destinatario}: {mensaje}")
            else:
                print(f"{remitente} a todos: {mensaje}")

# Ventajas:
# - Bajo acoplamiento: los colegas no se conocen entre sí
# - Centraliza la comunicación en un solo lugar
# - Facilita añadir nuevas funcionalidades
# - Simplifica la lógica de comunicación