# Sin patrón Mediator
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contactos = []
    
    def agregar_contacto(self, usuario):
        if usuario not in self.contactos:
            self.contactos.append(usuario)
            # Asegurar la conexión bidireccional
            if self not in usuario.contactos:
                usuario.agregar_contacto(self)
    
    def enviar_mensaje(self, mensaje, destinatario):
        print(f"{self.nombre} envía mensaje a {destinatario.nombre}: {mensaje}")
        destinatario.recibir_mensaje(mensaje, self)
    
    def enviar_mensaje_grupal(self, mensaje):
        print(f"{self.nombre} envía mensaje grupal: {mensaje}")
        for contacto in self.contactos:
            contacto.recibir_mensaje(mensaje, self)
    
    def recibir_mensaje(self, mensaje, remitente):
        print(f"{self.nombre} recibe mensaje de {remitente.nombre}: {mensaje}")

# Cliente
alice = Usuario("Alice")
bob = Usuario("Bob")
charlie = Usuario("Charlie")
dave = Usuario("Dave")

# Establecer conexiones directas entre usuarios
alice.agregar_contacto(bob)
alice.agregar_contacto(charlie)
bob.agregar_contacto(dave)
charlie.agregar_contacto(dave)

# Enviar mensajes directamente entre usuarios
alice.enviar_mensaje("Hola Bob", bob)
bob.enviar_mensaje("Hola Alice", alice)

# Enviar mensaje grupal
alice.enviar_mensaje_grupal("Hola a todos mis contactos")

# Problemas:
# - Alto acoplamiento: cada usuario debe conocer a todos sus contactos
# - Difícil mantener la consistencia en la comunicación
# - Difícil añadir nuevas funcionalidades o tipos de mensajes
# - Complejidad crece exponencialmente con el número de usuarios