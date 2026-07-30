# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05
LIMITE_COMISION_ALTA = 30000
LIMITE_BONO = 50000
MONTO_BONO = 500
ANCHO_REPORTE = 44

vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_total_vendedor(ventas_mensuales):
    if ventas_mensuales > LIMITE_COMISION_ALTA:
        tasa_comision = TASA_COMISION_ALTA
    else:
        tasa_comision = TASA_COMISION_BAJA

    comision = round(ventas_mensuales * tasa_comision, 2)

    if ventas_mensuales > LIMITE_BONO:
        bono = MONTO_BONO
    else:
        bono = 0

    return round(comision + bono, 2)


def calcular_comisiones():
    total_pagar = 0

    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    # recorre la lista
    for nombre_vendedor, ventas_mensuales in vendedores:
        total_vendedor = calcular_total_vendedor(ventas_mensuales)
        total_pagar = total_pagar + total_vendedor

        print(nombre_vendedor + ": Q " + str(total_vendedor))

    # ta = tp * 1.12
    # print("con iva", ta)

    print("-" * ANCHO_REPORTE)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))


calcular_comisiones()