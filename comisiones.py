# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona
COMISION_BASICA = 0.05
COMISION_SUPERIOR = 0.08

META_COMISION_SUPERIOR = 30000
META_BONO = 50000

BONO = 500

ANCHO_REPORTE = 44 


# lista de vendedores
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
        # si vendio mas de 30000
        if vendedor[1] > META_COMISION_SUPERIOR:
            # calcula la comision del 8%
            comision = vendedor[1] * COMISION_SUPERIOR
            comision = round(comision, 2)
            # el bono es de 300
            if vendedor[1] > META_BONO:
                bono = 500
            else:
                bono = 0
            total_vendedor = round(comision + bono, 2)
            total_pagar = total_pagar + total_vendedor
            print(vendedor[0] + ": Q " + str(total_vendedor))
        else:
            # calcula la comision del 5%
            comision = vendedor[1] * COMISION_BASICA
            comision = round(comision, 2)
            bono = 0
            total_vendedor = round(comision + bono, 2)
            total_pagar = total_pagar + total_vendedor
            print(vendedor[0] + ": Q " + str(total_vendedor))
    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * ANCHO_REPORTE)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))
 
calcular_comisiones()
