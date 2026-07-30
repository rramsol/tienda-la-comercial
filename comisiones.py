# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

ANCHO_REPORTE = 44
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BASE = 0.05
UMBRAL_BONO = 50000
MONTO_BONO = 500

# lista de vendedores
VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comisiones_mensuales():
    total_comisiones = 0

    print("=" * ANCHO_REPORTE)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)

    # recorre la lista
    for nombre_vendedor, ventas_mensuales in VENDEDORES:
        # si vendio mas de 30000
        if ventas_mensuales > UMBRAL_COMISION_ALTA:
            # calcula la comision del 8%
            comision = ventas_mensuales * TASA_COMISION_ALTA
            comision = round(comision, 2)

            # el bono es de 300
            if ventas_mensuales > UMBRAL_BONO:
                bono = MONTO_BONO
            else:
                bono = 0

            total_vendedor = round(comision + bono, 2)
            total_comisiones = total_comisiones + total_vendedor

            print(nombre_vendedor + ": Q " + str(total_vendedor))
        else:
            # calcula la comision del 5%
            comision = ventas_mensuales * TASA_COMISION_BASE
            comision = round(comision, 2)
            bono = 0

            total_vendedor = round(comision + bono, 2)
            total_comisiones = total_comisiones + total_vendedor

            print(nombre_vendedor + ": Q " + str(total_vendedor))

    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * ANCHO_REPORTE)
    print("Total a pagar: Q " + str(round(total_comisiones, 2)))


calcular_comisiones_mensuales()