# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05
LIMITE_COMISION_ALTA = 30000
LIMITE_BONO = 50000
MONTO_BONO = 500
ANCHO_REPORTE = 44

vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comisiones():
    total_pagar = 0

    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    # recorre la lista
    for vendedor in vendedores:
        nombre_vendedor = vendedor[0]
        ventas_mensuales = vendedor[1]

        # si vendio mas de 30000
        if ventas_mensuales > LIMITE_COMISION_ALTA:
            # calcula la comision del 8%
            comision = ventas_mensuales * TASA_COMISION_ALTA
            comision = round(comision, 2)

            # el bono es de 300
            if ventas_mensuales > LIMITE_BONO:
                bono = MONTO_BONO
            else:
                bono = 0

            total_vendedor = round(comision + bono, 2)
            total_pagar = total_pagar + total_vendedor

            print(nombre_vendedor + ": Q " + str(total_vendedor))
        else:
            # calcula la comision del 5%
            comision = ventas_mensuales * TASA_COMISION_BAJA
            comision = round(comision, 2)

            bono = 0
            total_vendedor = round(comision + bono, 2)
            total_pagar = total_pagar + total_vendedor

            print(nombre_vendedor + ": Q " + str(total_vendedor))

    # ta = tp * 1.12
    # print("con iva", ta)

    print("-" * ANCHO_REPORTE)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))


calcular_comisiones()