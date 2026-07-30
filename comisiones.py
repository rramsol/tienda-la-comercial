# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

# Valores utilizados en las reglas del negocio
ANCHO_REPORTE = 44
LIMITE_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
LIMITE_BONO = 50000
MONTO_BONO = 500
TASA_COMISION_BASE = 0.05
DECIMALES_MONEDA = 2

# lista de vendedores
ventas_vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comisiones():
    total_comisiones = 0

    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    # recorre la lista
    for nombre_vendedor, monto_ventas in ventas_vendedores:
        # si vendio mas de 30000
        if monto_ventas > LIMITE_COMISION_ALTA:
            # calcula la comision del 8%
            comision = monto_ventas * TASA_COMISION_ALTA
            comision = round(comision, DECIMALES_MONEDA)

            # el bono es de 300
            if monto_ventas > LIMITE_BONO:
                bono = MONTO_BONO
            else:
                bono = 0

            total_vendedor = round(
                comision + bono,
                DECIMALES_MONEDA,
            )
            total_comisiones = total_comisiones + total_vendedor

            print(
                nombre_vendedor
                + ": Q "
                + str(total_vendedor)
            )
        else:
            # calcula la comision del 5%
            comision = monto_ventas * TASA_COMISION_BASE
            comision = round(comision, DECIMALES_MONEDA)

            bono = 0

            total_vendedor = round(
                comision + bono,
                DECIMALES_MONEDA,
            )
            total_comisiones = total_comisiones + total_vendedor

            print(
                nombre_vendedor
                + ": Q "
                + str(total_vendedor)
            )

    # ta = tp * 1.12
    # print("con iva", ta)

    print("-" * ANCHO_REPORTE)
    print(
        "Total a pagar: Q "
        + str(round(total_comisiones, DECIMALES_MONEDA))
    )


calcular_comisiones()