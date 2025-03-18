# Sin patrón Chain of Responsibility
class SistemaAprobacion:
    def aprobar_gasto(self, monto, proposito):
        # Lógica de aprobación con condicionales anidados
        if monto <= 100:
            return self.aprobar_por_lider_equipo(monto, proposito)
        elif monto <= 1000:
            return self.aprobar_por_gerente(monto, proposito)
        elif monto <= 10000:
            return self.aprobar_por_director(monto, proposito)
        else:
            return self.aprobar_por_ceo(monto, proposito)
    
    def aprobar_por_lider_equipo(self, monto, proposito):
        return f"Líder de equipo aprueba gasto de ${monto} para {proposito}"
    
    def aprobar_por_gerente(self, monto, proposito):
        return f"Gerente aprueba gasto de ${monto} para {proposito}"
    
    def aprobar_por_director(self, monto, proposito):
        return f"Director aprueba gasto de ${monto} para {proposito}"
    
    def aprobar_por_ceo(self, monto, proposito):
        return f"CEO aprueba gasto de ${monto} para {proposito}"

# Cliente
sistema = SistemaAprobacion()
print(sistema.aprobar_gasto(50, "suministros de oficina"))
print(sistema.aprobar_gasto(500, "equipo nuevo"))
print(sistema.aprobar_gasto(5000, "conferencia"))
print(sistema.aprobar_gasto(20000, "renovación de oficina"))

# Problemas: 
# - Difícil de mantener y modificar si cambian las reglas de aprobación
# - Alta acoplamiento entre la clase y las reglas de negocio
# - Difícil añadir nuevos niveles de aprobación