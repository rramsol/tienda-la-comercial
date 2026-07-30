# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

META_VENTAS = 30000.00
META_BONO = 50000.00
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05
MONTO_BONO = 500

# lista de vendedores
vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]

def calcular_comisiones():
    total_comisiones = 0
    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)
    # recorre la lista
    for vendedor in vendedores:
        nombre_vendedor = vendedor[0]
        ventas_vendedor = vendedor[1]
        
        # si vendio mas de 30000
        if ventas_vendedor > META_VENTAS:
            # calcula la comision del 8%
            comision = ventas_vendedor * TASA_COMISION_ALTA
            comision = round(comision, 2)
            # el bono es de 300
            if ventas_vendedor > META_BONO:
                bono = MONTO_BONO
            else:
                bono = 0
            total_vendedor = round(comision + bono, 2)
            total_comisiones = total_comisiones + total_vendedor
            print(nombre_vendedor + ": Q " + str(total_vendedor))
        else:
            # calcula la comision del 5%
            comision = ventas_vendedor * TASA_COMISION_BAJA
            comision = round(comision, 2)
            bono = 0
            total_vendedor = round(comision + bono, 2)
            total_comisiones = total_comisiones + total_vendedor
            print(nombre_vendedor + ": Q " + str(total_vendedor))
    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_comisiones, 2)))

calcular_comisiones()