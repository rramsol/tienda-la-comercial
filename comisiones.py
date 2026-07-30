# -*- coding: utf-8 -*-
"""Genera el reporte mensual de comisiones de La Comercial."""

ANCHO_REPORTE = 44
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BASE = 0.05
UMBRAL_BONO = 50000
MONTO_BONO = 500
DECIMALES_MONEDA = 2

VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(ventas):
    """Calcula la comisión correspondiente al monto vendido."""

    # La regla original exige superar el umbral, no solamente alcanzarlo.
    if ventas > UMBRAL_COMISION_ALTA:
        return round(
            ventas * TASA_COMISION_ALTA,
            DECIMALES_MONEDA
        )

    return round(
        ventas * TASA_COMISION_BASE,
        DECIMALES_MONEDA
    )


def calcular_bono(ventas):
    """Calcula el bono adicional según el monto vendido."""

    # El bono se concede únicamente cuando las ventas superan el umbral.
    if ventas > UMBRAL_BONO:
        return MONTO_BONO

    return 0


def calcular_pago_vendedor(ventas):
    """Devuelve la suma de la comisión y el bono del vendedor."""

    comision = calcular_comision(ventas)
    bono = calcular_bono(ventas)

    return round(
        comision + bono,
        DECIMALES_MONEDA
    )


def imprimir_reporte_comisiones():
    """Imprime el detalle de pagos y el total mensual de comisiones."""

    total_pagar = 0

    print("=" * ANCHO_REPORTE)
    print(" COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, ventas in VENDEDORES:
        total_vendedor = calcular_pago_vendedor(ventas)
        total_pagar = total_pagar + total_vendedor

        print(nombre_vendedor + ": Q " + str(total_vendedor))

    print("-" * ANCHO_REPORTE)
    print(
        "Total a pagar: Q "
        + str(round(total_pagar, DECIMALES_MONEDA))
    )


imprimir_reporte_comisiones()