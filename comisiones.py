# -*- coding: utf-8 -*-
"""
Programa para calcular las comisiones mensuales de los vendedores.
"""

LIMITE_COMISION_ALTA = 30000
LIMITE_BONO = 50000
COMISION_BAJA = 0.05
COMISION_ALTA = 0.08
BONO = 500

VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(ventas):
    """Calcula la comisión según el monto de ventas."""
    if ventas > LIMITE_COMISION_ALTA:
        return round(ventas * COMISION_ALTA, 2)
    return round(ventas * COMISION_BAJA, 2)


def calcular_bono(ventas):
    """Otorga un bono adicional cuando se supera la meta mensual."""
    if ventas > LIMITE_BONO:
        return BONO
    return 0


def imprimir_reporte(vendedores):
    """Muestra el reporte de comisiones del mes."""
    total_pagar = 0

    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)

    for nombre, ventas in vendedores:
        comision = calcular_comision(ventas)
        bono = calcular_bono(ventas)

        total = round(comision + bono, 2)
        total_pagar += total

        print(nombre + ": Q " + str(total))

    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))


def calcular_comisiones():
    """Coordina el proceso de cálculo e impresión del reporte."""
    imprimir_reporte(VENDEDORES)


calcular_comisiones()