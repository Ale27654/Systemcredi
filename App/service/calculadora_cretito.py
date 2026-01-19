from servicio.capacidad_pago import capacidad_pago

def cuota_mensual(monto, plazo_meses, tasa=0.02):
    return round((monto * (1 + tasa)) / plazo_meses, 2)

def es_credito_viable(ingresos, gastos, monto, plazo_meses):
    cuota = cuota_mensual(monto, plazo_meses)
    disponible = capacidad_pago(ingresos, gastos)
    return disponible >= cuota
