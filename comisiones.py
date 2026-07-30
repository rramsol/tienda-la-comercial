# -*- coding: utf-8 -*-
"""Calcula e imprime las comisiones mensuales de La Comercial."""

ANCHO_REPORTE = 44
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
UMBRAL_BONO = 50000
MONTO_BONO = 500
TASA_COMISION_BASE = 0.05
DECIMALES_MONEDA = 2

VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_pago_vendedor(ventas_mensuales):
    """Calcula la comisión y el bono según las ventas mensuales."""

    if ventas_mensuales > UMBRAL_COMISION_ALTA:
        tasa_comision = TASA_COMISION_ALTA

        # El bono premia únicamente a quienes superan el umbral definido.
        if ventas_mensuales > UMBRAL_BONO:
            bono = MONTO_BONO
        else:
            bono = 0
    else:
        tasa_comision = TASA_COMISION_BASE
        bono = 0

    comision = round(
        ventas_mensuales * tasa_comision,
        DECIMALES_MONEDA
    )

    return round(
        comision + bono,
        DECIMALES_MONEDA
    )


def imprimir_reporte_comisiones():
    """Imprime las comisiones individuales y el total mensual."""

    total_a_pagar = 0

    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, ventas_mensuales in VENDEDORES:
        total_vendedor = calcular_pago_vendedor(ventas_mensuales)
        total_a_pagar = total_a_pagar + total_vendedor

        print(
            nombre_vendedor
            + ": Q "
            + str(total_vendedor)
        )

    print("-" * ANCHO_REPORTE)
    print(
        "Total a pagar: Q "
        + str(round(total_a_pagar, DECIMALES_MONEDA))
    )


imprimir_reporte_comisiones()