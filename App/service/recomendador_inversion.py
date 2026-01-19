def recomendar_inversion(capacidad_ahorro):
    if capacidad_ahorro <= 0:
        return "No se recomienda invertir en este momento."
    elif capacidad_ahorro < 200000:
        return "Inversión conservadora (ahorro programado)."
    else:
        return "Inversión moderada (fondos o CDT)."
