# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

ANCHO_REPORTE = 44
DECIMALES_MONEDA = 2
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BASE = 0.05
UMBRAL_BONO = 50000
MONTO_BONO = 500
SIN_BONO = 0

# lista de vendedores
VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def obtener_tasa_comision(ventas_mensuales):
    # si vendio mas de 30000
    if ventas_mensuales > UMBRAL_COMISION_ALTA:
        # calcula la comision del 8%
        return TASA_COMISION_ALTA

    # calcula la comision del 5%
    return TASA_COMISION_BASE


def calcular_bono(ventas_mensuales):
    # el bono es de 300
    if ventas_mensuales > UMBRAL_BONO:
        return MONTO_BONO

    return SIN_BONO


def calcular_pago_comision(ventas_mensuales):
    tasa_comision = obtener_tasa_comision(ventas_mensuales)

    comision = round(
        ventas_mensuales * tasa_comision,
        DECIMALES_MONEDA,
    )

    bono = calcular_bono(ventas_mensuales)

    return round(
        comision + bono,
        DECIMALES_MONEDA,
    )


def calcular_pagos_vendedores(vendedores):
    pagos_vendedores = []
    total_comisiones = 0

    # recorre la lista
    for nombre_vendedor, ventas_mensuales in vendedores:
        pago_total = calcular_pago_comision(ventas_mensuales)

        pagos_vendedores.append(
            (nombre_vendedor, pago_total)
        )

        total_comisiones = total_comisiones + pago_total

    return (
        pagos_vendedores,
        round(total_comisiones, DECIMALES_MONEDA),
    )


def imprimir_reporte_comisiones(
    pagos_vendedores,
    total_comisiones,
):
    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, pago_total in pagos_vendedores:
        print(nombre_vendedor + ": Q " + str(pago_total))

    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * ANCHO_REPORTE)
    print("Total a pagar: Q " + str(total_comisiones))


def ejecutar_reporte_comisiones():
    pagos_vendedores, total_comisiones = (
        calcular_pagos_vendedores(VENDEDORES)
    )

    imprimir_reporte_comisiones(
        pagos_vendedores,
        total_comisiones,
    )


ejecutar_reporte_comisiones()