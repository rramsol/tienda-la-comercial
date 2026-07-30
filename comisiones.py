# -*- coding: utf-8 -*-
"""Calcula e imprime las comisiones mensuales de los vendedores."""

ANCHO_REPORTE = 44
META_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
META_BONO = 50000
MONTO_BONO = 500
SIN_BONO = 0
TASA_COMISION_BASE = 0.05
DECIMALES_MONEDA = 2

vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(ventas_mensuales):
    # La meta debe superarse; igualarla mantiene la tasa base.
    if ventas_mensuales > META_COMISION_ALTA:
        tasa_comision = TASA_COMISION_ALTA
    else:
        tasa_comision = TASA_COMISION_BASE

    # Se conserva el redondeo intermedio para no alterar la regla actual.
    return round(
        ventas_mensuales * tasa_comision,
        DECIMALES_MONEDA
    )


def calcular_bono(ventas_mensuales):
    # El bono se entrega únicamente cuando las ventas superan la meta.
    if ventas_mensuales > META_BONO:
        return MONTO_BONO

    return SIN_BONO


def calcular_pago_vendedor(ventas_mensuales):
    comision = calcular_comision(ventas_mensuales)
    bono = calcular_bono(ventas_mensuales)

    return round(
        comision + bono,
        DECIMALES_MONEDA
    )


def calcular_pagos():
    pagos_vendedores = []
    total_pagar = 0

    for nombre_vendedor, ventas_mensuales in vendedores:
        total_vendedor = calcular_pago_vendedor(ventas_mensuales)

        pagos_vendedores.append(
            (nombre_vendedor, total_vendedor)
        )

        total_pagar = total_pagar + total_vendedor

    return pagos_vendedores, total_pagar


def imprimir_reporte(pagos_vendedores, total_pagar):
    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, total_vendedor in pagos_vendedores:
        print(
            nombre_vendedor
            + ": Q "
            + str(total_vendedor)
        )

    print("-" * ANCHO_REPORTE)
    print(
        "Total a pagar: Q "
        + str(round(total_pagar, DECIMALES_MONEDA))
    )


def generar_reporte_comisiones():
    pagos_vendedores, total_pagar = calcular_pagos()
    imprimir_reporte(pagos_vendedores, total_pagar)


generar_reporte_comisiones()