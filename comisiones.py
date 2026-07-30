# -*- coding: utf-8 -*-

# programa de comisiones
# hecho por kevin, no tocar, ya funciona

COMISION_BASICA = 0.05
COMISION_SUPERIOR = 0.08

META_COMISION_SUPERIOR = 30000
META_BONO = 50000

BONO = 500

ANCHO_REPORTE = 44


vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_total_vendedor(ventas):
    if ventas > META_COMISION_SUPERIOR:
        porcentaje_comision = COMISION_SUPERIOR
    else:
        porcentaje_comision = COMISION_BASICA

    comision = round(ventas * porcentaje_comision, 2)

    if ventas > META_BONO:
        bono = BONO
    else:
        bono = 0

    return round(comision + bono, 2)


def calcular_comisiones():
    total_pagar = 0

    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    for vendedor in vendedores:
        total_vendedor = calcular_total_vendedor(vendedor[1])
        total_pagar += total_vendedor
        print(vendedor[0] + ": Q " + str(total_vendedor))

    print("-" * ANCHO_REPORTE)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))


calcular_comisiones()