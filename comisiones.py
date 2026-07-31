# -*- coding: utf-8 -*-
"""Calcula y muestra las comisiones mensuales de La Comercial."""

ANCHO_REPORTE = 44
DECIMALES_MONEDA = 2
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BASE = 0.05
UMBRAL_BONO = 50000
MONTO_BONO = 500
SIN_BONO = 0

VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def obtener_tasa_comision(ventas_mensuales):
    """Devuelve la tasa aplicable según las ventas mensuales."""
    if ventas_mensuales > UMBRAL_COMISION_ALTA:
        return TASA_COMISION_ALTA

    return TASA_COMISION_BASE


def calcular_bono(ventas_mensuales):
    """Devuelve el bono aplicable según las ventas mensuales."""
    if ventas_mensuales > UMBRAL_BONO:
        return MONTO_BONO

    return SIN_BONO


def calcular_pago_comision(ventas_mensuales):
    """Calcula la comisión y el bono de un vendedor."""
    tasa_comision = obtener_tasa_comision(ventas_mensuales)

    # Se redondea la comisión antes de sumar el bono para conservar
    # exactamente la regla de cálculo del programa original.
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
    """Calcula los pagos individuales y el total mensual."""
    pagos_vendedores = []
    total_comisiones = 0

    for nombre_vendedor, ventas_mensuales in vendedores:
        pago_total = calcular_pago_comision(ventas_mensuales)

        pagos_vendedores.append(
            (nombre_vendedor, pago_total)
        )

        # El total usa los pagos ya redondeados para conservar
        # el mismo resultado del programa original.
        total_comisiones = total_comisiones + pago_total

    return (
        pagos_vendedores,
        round(total_comisiones, DECIMALES_MONEDA),
    )


def imprimir_reporte_comisiones(
    pagos_vendedores,
    total_comisiones,
):
    """Muestra el reporte sin modificar su formato original."""
    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, pago_total in pagos_vendedores:
        print(nombre_vendedor + ": Q " + str(pago_total))

    print("-" * ANCHO_REPORTE)
    print("Total a pagar: Q " + str(total_comisiones))


def ejecutar_reporte_comisiones():
    """Coordina el cálculo y la impresión del reporte."""
    pagos_vendedores, total_comisiones = (
        calcular_pagos_vendedores(VENDEDORES)
    )

    imprimir_reporte_comisiones(
        pagos_vendedores,
        total_comisiones,
    )


ejecutar_reporte_comisiones()