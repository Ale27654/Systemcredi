class Credito:
    def __init__(self, ingresos, gastos, monto, plazo_meses, tasa=0.02):
        self.ingresos = ingresos
        self.gastos = gastos
        self.monto = monto
        self.plazo = plazo_meses
        self.tasa = tasa

    def capacidad_pago(self):
        return self.ingresos - self.gastos

    def cuota_mensual(self):
        return round((self.monto * (1 + self.tasa)) / self.plazo, 2)

    def es_viable(self):
        return self.capacidad_pago() >= self.cuota_mensual()
