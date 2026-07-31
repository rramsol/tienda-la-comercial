# -*- coding: utf-8 -*-
"""Calcula e imprime las comisiones mensuales de los vendedores."""

ANCHO_REPORTE = 44
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BASE = 0.05
UMBRAL_BONO = 50000
MONTO_BONO = 500

VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(ventas_mensuales):
    if ventas_mensuales > UMBRAL_COMISION_ALTA:
        tasa_comision = TASA_COMISION_ALTA
    else:
        tasa_comision = TASA_COMISION_BASE

    return round(ventas_mensuales * tasa_comision, 2)


def calcular_bono(ventas_mensuales):
    if ventas_mensuales > UMBRAL_BONO:
        return MONTO_BONO

    return 0


def calcular_pago_vendedor(ventas_mensuales):
    comision = calcular_comision(ventas_mensuales)
    bono = calcular_bono(ventas_mensuales)

    return round(comision + bono, 2)


def calcular_pagos_mensuales(vendedores):
    pagos_vendedores = []
    total_comisiones = 0

    for nombre_vendedor, ventas_mensuales in vendedores:
        total_vendedor = calcular_pago_vendedor(ventas_mensuales)
        pagos_vendedores.append((nombre_vendedor, total_vendedor))
        total_comisiones = total_comisiones + total_vendedor

    return pagos_vendedores, round(total_comisiones, 2)


def imprimir_reporte(pagos_vendedores, total_comisiones):
    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, total_vendedor in pagos_vendedores:
        print(nombre_vendedor + ": Q " + str(total_vendedor))

    print("-" * ANCHO_REPORTE)
    print("Total a pagar: Q " + str(total_comisiones))


def generar_reporte_comisiones():
    pagos_vendedores, total_comisiones = calcular_pagos_mensuales(VENDEDORES)
    imprimir_reporte(pagos_vendedores, total_comisiones)


generar_reporte_comisiones()