# -*- coding: utf-8 -*-

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
    """Calcula la comisión según el nivel mensual de ventas."""
    if ventas > UMBRAL_COMISION_ALTA:
        tasa_comision = TASA_COMISION_ALTA
    else:
        tasa_comision = TASA_COMISION_BASE

    return round(ventas * tasa_comision, DECIMALES_MONEDA)


def calcular_bono(ventas):
    """Devuelve el bono adicional cuando se supera la meta establecida."""
    if ventas > UMBRAL_BONO:
        return BONO_VENTAS_ALTAS

    return SIN_BONO


def calcular_pago_vendedor(ventas):
    """Calcula el pago total de comisión y bono de un vendedor."""
    comision = calcular_comision(ventas)
    bono = calcular_bono(ventas)

    return round(comision + bono, DECIMALES_MONEDA)


def calcular_pagos(vendedores):
    """Calcula los pagos individuales y el total general."""
    pagos = []
    total_a_pagar = 0

    for nombre_vendedor, ventas in vendedores:
        total_vendedor = calcular_pago_vendedor(ventas)
        pagos.append((nombre_vendedor, total_vendedor))
        total_a_pagar = total_a_pagar + total_vendedor

    return pagos, total_a_pagar


def imprimir_reporte(pagos, total_a_pagar):
    """Imprime el reporte mensual de comisiones."""
    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, total_vendedor in pagos:
        print(nombre_vendedor + ": Q " + str(total_vendedor))

    print("-" * ANCHO_REPORTE)
    print(
        "Total a pagar: Q "
        + str(round(total_a_pagar, DECIMALES_MONEDA))
    )


def generar_reporte_comisiones():
    """Coordina el cálculo y la presentación del reporte."""
    pagos, total_a_pagar = calcular_pagos(VENDEDORES)
    imprimir_reporte(pagos, total_a_pagar)


generar_reporte_comisiones()