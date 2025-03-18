# Con patrón Singleton
class DatabaseConnectionWithSingleton:
    _instance = None
    
    def __new__(cls, host=None, user=None, password=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.host = host
            cls._instance.user = user
            cls._instance.password = password
            print(f"Conectando a la base de datos en {cls._instance.host}")
            # Lógica de conexión a la base de datos...
        return cls._instance

# Ahora sólo se crea una conexión
conn1 = DatabaseConnectionWithSingleton("servidor1.ejemplo.com", "usuario", "contraseña")
conn2 = DatabaseConnectionWithSingleton()  # No requiere parámetros, usa la instancia existente
conn3 = DatabaseConnectionWithSingleton()  # También usa la misma instancia

# Todas las variables apuntan al mismo objeto
print(f"¿Son la misma conexión? {conn1 is conn2}")  # True

# Modificar cualquier instancia afecta a todas
conn1.host = "servidor2.ejemplo.com"
print(f"Host de conn2: {conn2.host}")  # servidor2.ejemplo.com
