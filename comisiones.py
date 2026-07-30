# -*- coding: utf-8 -*-
"""Cálculo de comisiones mensuales de vendedores para La Comercial."""

# Reglas de negocio definidas por gerencia
UMBRAL_VENTA_ALTA = 30000   # a partir de aquí aplica la tasa alta
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05
UMBRAL_BONO = 50000          # ventas superiores a esto reciben bono fijo
BONO = 500

vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(venta):
    """Calcula la comisión + bono de un vendedor según su venta."""
    if venta > UMBRAL_VENTA_ALTA:
        comision = round(venta * TASA_COMISION_ALTA, 2)
        bono = BONO if venta > UMBRAL_BONO else 0
    else:
        comision = round(venta * TASA_COMISION_BAJA, 2)
        bono = 0
    return round(comision + bono, 2)


def calcular_comisiones():
    """Imprime el reporte de comisiones del mes y el total a pagar."""
    total_pagar = 0
    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)
    for nombre, venta in vendedores:
        total_vendedor = calcular_comision(venta)
        total_pagar += total_vendedor
        print(nombre + ": Q " + str(total_vendedor))
    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))


calcular_comisiones()