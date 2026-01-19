from servicio import (
    cuota_mensual,
    es_credito_viable,
    proyeccion_pagos,
    recomendar_inversion,
    recordatorio_pago
)

ingresos = 2000000
gastos = 1200000
monto = 3000000
plazo = 12

print("Cuota:", cuota_mensual(monto, plazo))
print("¿Viable?:", es_credito_viable(ingresos, gastos, monto, plazo))

print(proyeccion_pagos(monto, cuota_mensual(monto, plazo), plazo))
print(recomendar_inversion(ingresos - gastos))
print(recordatorio_pago("2026-02-10", cuota_mensual(monto, plazo)))
