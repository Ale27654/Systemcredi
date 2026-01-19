def proyeccion_pagos(monto, cuota, meses):
    saldo = monto
    historial = []

    for mes in range(1, meses + 1):
        saldo -= cuota
        saldo = max(saldo, 0)
        historial.append({
            "mes": mes,
            "saldo_restante": saldo
        })

    return historial
