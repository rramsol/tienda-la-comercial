# -*- coding: utf-8 -*-
"""Calculo e impresion de las comisiones mensuales de los vendedores de La Comercial."""

VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]

ANCHO_SEPARADOR = 44
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05
UMBRAL_BONO = 50000
MONTO_BONO = 500


def calcular_comision(monto_ventas):
    if monto_ventas > UMBRAL_COMISION_ALTA:
        comision = monto_ventas * TASA_COMISION_ALTA
    else:
        comision = monto_ventas * TASA_COMISION_BAJA
    return round(comision, 2)


def calcular_bono(monto_ventas):
    # bono fijo (no porcentual): asi lo definio gerencia para premiar el hito de 50000
    if monto_ventas > UMBRAL_BONO:
        return MONTO_BONO
    return 0


def calcular_total_vendedor(monto_ventas):
    return round(calcular_comision(monto_ventas) + calcular_bono(monto_ventas), 2)


def calcular_comisiones(vendedores):
    return [(nombre, calcular_total_vendedor(ventas)) for nombre, ventas in vendedores]


def imprimir_reporte(totales):
    print("=" * ANCHO_SEPARADOR)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_SEPARADOR)
    total_pagado = 0
    for nombre, total in totales:
        total_pagado = total_pagado + total
        print(nombre + ": Q " + str(total))
    print("-" * ANCHO_SEPARADOR)
    print("Total a pagar: Q " + str(round(total_pagado, 2)))


imprimir_reporte(calcular_comisiones(VENDEDORES))
