# -*- coding: utf-8 -*-
"""Calcula y muestra las comisiones mensuales de los vendedores."""

COMISION_ALTA = 0.08
COMISION_BAJA = 0.05
META_COMISION = 30000
META_BONO = 50000
BONO = 500

vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_pago(ventas):
    """Calcula la comisión y el bono correspondiente."""

    if ventas > META_COMISION:
        comision = round(ventas * COMISION_ALTA, 2)
        bono = BONO if ventas > META_BONO else 0
    else:
        comision = round(ventas * COMISION_BAJA, 2)
        bono = 0

    return round(comision + bono, 2)


def calcular_comisiones():
    """Genera el reporte mensual de comisiones."""

    total_pagar = 0

    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)

    for nombre, ventas in vendedores:
        pago = calcular_pago(ventas)
        total_pagar += pago
        print(nombre + ": Q " + str(pago))

    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))


calcular_comisiones()