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

def calcular_comision_vendedor(venta):
    """Calcula la comisión y bono para un monto de venta.
    
    Vendedores con venta > 30000 reciben 8% de comisión.
    Vendedores con venta <= 30000 reciben 5% de comisión.
    Si venta > 50000, agrega bono de 500 quetzales.
    """
    if venta > UMBRAL_COMISION_ALTA:
        comision = venta * TASA_COMISION_ALTA
        bono = MONTO_BONO if venta > UMBRAL_BONO else 0
    else:
        comision = venta * TASA_COMISION_BAJA
        bono = 0
    
    return round(comision + bono, 2)

def calcular_comisiones():
    """Imprime el reporte de comisiones mensuales."""
    total_pagar = 0
    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)
    
    for nombre_vendedor, venta in vendedores:
        total_vendedor = calcular_comision_vendedor(venta)
        total_pagar = total_pagar + total_vendedor
        print(nombre_vendedor + ": Q " + str(total_vendedor))
    
    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))

calcular_comisiones()