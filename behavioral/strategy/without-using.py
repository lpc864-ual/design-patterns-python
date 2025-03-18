# Sin patrón Strategy
class CalculadoraImpuestos:
    def calcular_impuesto(self, tipo_impuesto, monto):
        if tipo_impuesto == "IVA":
            # Impuesto al Valor Agregado: 21%
            return monto * 0.21
        elif tipo_impuesto == "IRPF":
            # Impuesto sobre la Renta: 15% hasta 30000, 20% para el resto
            if monto <= 30000:
                return monto * 0.15
            else:
                return 30000 * 0.15 + (monto - 30000) * 0.20
        elif tipo_impuesto == "IS":
            # Impuesto de Sociedades: 25% con deducciones
            base_imponible = monto * 0.90  # 10% de gastos deducibles
            return base_imponible * 0.25
        else:
            raise ValueError(f"Tipo de impuesto desconocido: {tipo_impuesto}")

# Cliente
calculadora = CalculadoraImpuestos()

# Calcular diferentes impuestos
monto_compra = 1000
impuesto_iva = calculadora.calcular_impuesto("IVA", monto_compra)
print(f"Impuesto IVA para {monto_compra}€: {impuesto_iva}€")

salario_anual = 45000
impuesto_renta = calculadora.calcular_impuesto("IRPF", salario_anual)
print(f"Impuesto sobre la renta para {salario_anual}€: {impuesto_renta}€")

beneficio_empresa = 100000
impuesto_sociedades = calculadora.calcular_impuesto("IS", beneficio_empresa)
print(f"Impuesto de sociedades para {beneficio_empresa}€: {impuesto_sociedades}€")

# Problemas:
# - Cada vez que se añade un nuevo tipo de impuesto, hay que modificar la clase
# - Difícil mantener algoritmos complejos dentro de la misma clase
# - Alto acoplamiento entre la calculadora y los algoritmos de cálculo
# - Violación del principio Open/Closed