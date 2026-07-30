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


def calcular_comisiones():
    total_a_pagar = 0

    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    # recorre la lista
    for vendedor in VENDEDORES:
        # si vendio mas de 30000
        if vendedor[1] > UMBRAL_COMISION_ALTA:
            # calcula la comision del 8%
            comision = vendedor[1] * TASA_COMISION_ALTA
            comision = round(comision, DECIMALES_MONEDA)

            # el bono es de 300
            if vendedor[1] > UMBRAL_BONO:
                bono = BONO_VENTAS_ALTAS
            else:
                bono = SIN_BONO

            total_vendedor = round(
                comision + bono,
                DECIMALES_MONEDA,
            )
            total_a_pagar = total_a_pagar + total_vendedor

            print(vendedor[0] + ": Q " + str(total_vendedor))
        else:
            # calcula la comision del 5%
            comision = vendedor[1] * TASA_COMISION_BASE
            comision = round(comision, DECIMALES_MONEDA)
            bono = SIN_BONO

            total_vendedor = round(
                comision + bono,
                DECIMALES_MONEDA,
            )
            total_a_pagar = total_a_pagar + total_vendedor

            print(vendedor[0] + ": Q " + str(total_vendedor))

    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * ANCHO_REPORTE)
    print(
        "Total a pagar: Q "
        + str(round(total_a_pagar, DECIMALES_MONEDA))
    )


calcular_comisiones()