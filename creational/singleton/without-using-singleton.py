# Sin patrón Singleton
class DatabaseConnectionWithoutSingleton:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        print(f"Conectando a la base de datos en {self.host}")
        # Lógica de conexión a la base de datos...

# Problema: múltiples conexiones innecesarias
conn1 = DatabaseConnectionWithoutSingleton("servidor1.ejemplo.com", "usuario", "contraseña")
conn2 = DatabaseConnectionWithoutSingleton("servidor1.ejemplo.com", "usuario", "contraseña")
conn3 = DatabaseConnectionWithoutSingleton("servidor1.ejemplo.com", "usuario", "contraseña")

# Cada conexión es un objeto diferente
print(f"¿Son la misma conexión? {conn1 is conn2}")  # False

# Esto podría causar problemas de recursos y consistencia en una aplicación real
