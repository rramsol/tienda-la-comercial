# -*- coding: utf-8 -*-
# Módulo de cálculo de comisiones mensuales para vendedores

UMBRAL_COMISION_ALTA = 30000
UMBRAL_BONO = 50000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05
MONTO_BONO = 500

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
    
    for vendedor in vendedores:
        nombre_vendedor = vendedor[0]
        venta = vendedor[1]
        
        if venta > UMBRAL_COMISION_ALTA:
            comision = venta * TASA_COMISION_ALTA
            comision = round(comision, 2)
            
            if venta > UMBRAL_BONO:
                bono = MONTO_BONO
            else:
                bono = 0
            
            total_vendedor = round(comision + bono, 2)
            total_pagar = total_pagar + total_vendedor
            print(nombre_vendedor + ": Q " + str(total_vendedor))
        else:
            comision = venta * TASA_COMISION_BAJA
            comision = round(comision, 2)
            bono = 0
            total_vendedor = round(comision + bono, 2)
            total_pagar = total_pagar + total_vendedor
            print(nombre_vendedor + ": Q " + str(total_vendedor))
    
    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))

calcular_comisiones()