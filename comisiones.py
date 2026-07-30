# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

UMBRAL_VENTA_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05
UMBRAL_BONO = 50000
BONO = 500

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
    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)
    # recorre la lista
    for nombre, venta in vendedores:
        # si vendio mas de UMBRAL_VENTA_ALTA
        if venta > UMBRAL_VENTA_ALTA:
            # calcula la comision alta
            comision = round(venta * TASA_COMISION_ALTA, 2)
            # el bono es de BONO
            if venta > UMBRAL_BONO:
                bono = BONO
            else:
                bono = 0
            total_vendedor = round(comision + bono, 2)
            total_pagar = total_pagar + total_vendedor
            print(nombre + ": Q " + str(total_vendedor))
        else:
            # calcula la comision baja
            comision = round(venta * TASA_COMISION_BAJA, 2)
            bono = 0
            total_vendedor = round(comision + bono, 2)
            total_pagar = total_pagar + total_vendedor
            print(nombre + ": Q " + str(total_vendedor))
    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))

calcular_comisiones()