# -*- coding: utf-8 -*-

"""Calcula y muestra las comisiones mensuales de los vendedores."""

ANCHO_REPORTE = 44
LIMITE_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
LIMITE_BONO = 50000
MONTO_BONO = 500
TASA_COMISION_BASE = 0.05
DECIMALES_MONEDA = 2

ventas_vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(monto_ventas):
    """Calcula la comision correspondiente al monto vendido."""

    # La tasa alta aplica solo cuando se supera el limite.
    if monto_ventas > LIMITE_COMISION_ALTA:
        tasa_comision = TASA_COMISION_ALTA
    else:
        tasa_comision = TASA_COMISION_BASE

    comision = monto_ventas * tasa_comision

    return round(comision, DECIMALES_MONEDA)


def calcular_bono(monto_ventas):
    """Calcula el bono adicional por superar la meta de ventas."""

    # La regla exige superar la meta, no solamente igualarla.
    if monto_ventas > LIMITE_BONO:
        return MONTO_BONO

    return 0


def calcular_pago_vendedor(monto_ventas):
    """Calcula el pago total de comision y bono."""

    comision = calcular_comision(monto_ventas)
    bono = calcular_bono(monto_ventas)

    total_vendedor = comision + bono

    return round(total_vendedor, DECIMALES_MONEDA)


def calcular_comisiones(vendedores):
    """Calcula los pagos individuales y el total general."""

    pagos_vendedores = []
    total_comisiones = 0

    for nombre_vendedor, monto_ventas in vendedores:
        total_vendedor = calcular_pago_vendedor(
            monto_ventas
        )

        pagos_vendedores.append(
            (nombre_vendedor, total_vendedor)
        )

        total_comisiones = (
            total_comisiones + total_vendedor
        )

    total_comisiones = round(
        total_comisiones,
        DECIMALES_MONEDA,
    )

    return pagos_vendedores, total_comisiones


def imprimir_reporte(pagos_vendedores, total_comisiones):
    """Muestra el reporte mensual conservando su formato original."""

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
        + str(total_comisiones)
    )


pagos_vendedores, total_comisiones = calcular_comisiones(
    ventas_vendedores
)

imprimir_reporte(
    pagos_vendedores,
    total_comisiones,
)