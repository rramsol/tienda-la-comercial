# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

ANCHO_REPORTE = 44
UMBRAL_COMISION_ALTA = 30000
UMBRAL_BONO = 50000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BASE = 0.05
BONO_VENTAS_ALTAS = 500
SIN_BONO = 0
DECIMALES_MONEDA = 2

VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(ventas):
    # si vendio mas de 30000
    if ventas > UMBRAL_COMISION_ALTA:
        # calcula la comision del 8%
        tasa_comision = TASA_COMISION_ALTA
    else:
        # calcula la comision del 5%
        tasa_comision = TASA_COMISION_BASE

    return round(ventas * tasa_comision, DECIMALES_MONEDA)


def calcular_bono(ventas):
    # el bono es de 300
    if ventas > UMBRAL_BONO:
        return BONO_VENTAS_ALTAS

    return SIN_BONO


def calcular_pago_vendedor(ventas):
    comision = calcular_comision(ventas)
    bono = calcular_bono(ventas)

    return round(comision + bono, DECIMALES_MONEDA)


def calcular_pagos(vendedores):
    pagos = []
    total_a_pagar = 0

    # recorre la lista
    for nombre_vendedor, ventas in vendedores:
        total_vendedor = calcular_pago_vendedor(ventas)
        pagos.append((nombre_vendedor, total_vendedor))
        total_a_pagar = total_a_pagar + total_vendedor

    return pagos, total_a_pagar


def imprimir_reporte(pagos, total_a_pagar):
    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, total_vendedor in pagos:
        print(nombre_vendedor + ": Q " + str(total_vendedor))

    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * ANCHO_REPORTE)
    print(
        "Total a pagar: Q "
        + str(round(total_a_pagar, DECIMALES_MONEDA))
    )


def generar_reporte_comisiones():
    pagos, total_a_pagar = calcular_pagos(VENDEDORES)
    imprimir_reporte(pagos, total_a_pagar)


generar_reporte_comisiones()