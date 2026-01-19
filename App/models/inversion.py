class Inversion:
    def __init__(self, monto, rendimiento):
        self.monto = monto
        self.rendimiento = rendimiento

    def valor_final(self):
        return self.monto * (1 + self.rendimiento)
