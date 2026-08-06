# -*- coding: utf-8 -*-
"""Calcula y muestra las comisiones mensuales de los vendedores.

El módulo conserva las reglas actuales del negocio:
- La comisión base es del 5 %.
- La comisión alta es del 8 % cuando las ventas superan Q30,000.
- Se entrega un bono de Q500 cuando las ventas superan Q50,000.
"""

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


def obtener_tasa_comision(ventas_mensuales):
    """Devuelve la tasa de comisión que corresponde al total vendido."""

    # La regla utiliza "mayor que", por lo que exactamente Q30,000
    # todavía recibe la tasa base.
    if ventas_mensuales > UMBRAL_COMISION_ALTA:
        return TASA_COMISION_ALTA

    return TASA_COMISION_BASE


def calcular_bono(ventas_mensuales):
    """Devuelve el bono adicional correspondiente al nivel de ventas."""

    # El bono se entrega únicamente cuando se supera el umbral;
    # una venta exactamente igual a Q50,000 no lo recibe.
    if ventas_mensuales > UMBRAL_BONO:
        return MONTO_BONO

    return 0


def calcular_total_vendedor(ventas_mensuales):
    """Calcula la comisión y el bono total de un vendedor."""

    tasa_comision = obtener_tasa_comision(ventas_mensuales)

    comision = ventas_mensuales * tasa_comision
    comision = round(comision, DECIMALES_MONEDA)

    bono = calcular_bono(ventas_mensuales)

    total_vendedor = round(
        comision + bono,
        DECIMALES_MONEDA,
    )

    return total_vendedor


def calcular_comisiones(vendedores):
    """Calcula los resultados individuales y el total general."""

    comisiones_vendedores = []
    total_comisiones = 0

    for nombre_vendedor, ventas_mensuales in vendedores:
        total_vendedor = calcular_total_vendedor(ventas_mensuales)

        comisiones_vendedores.append(
            (nombre_vendedor, total_vendedor)
        )

        total_comisiones = total_comisiones + total_vendedor

    total_comisiones = round(
        total_comisiones,
        DECIMALES_MONEDA,
    )

    return comisiones_vendedores, total_comisiones


def imprimir_reporte_comisiones(
    comisiones_vendedores,
    total_comisiones,
):
    """Muestra el reporte mensual sin realizar cálculos de negocio."""

    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for nombre_vendedor, total_vendedor in comisiones_vendedores:
        print(nombre_vendedor + ": Q " + str(total_vendedor))

    print("-" * ANCHO_REPORTE)
    print("Total a pagar: Q " + str(total_comisiones))


comisiones_vendedores, total_comisiones = calcular_comisiones(
    VENDEDORES
)

imprimir_reporte_comisiones(
    comisiones_vendedores,
    total_comisiones,
)