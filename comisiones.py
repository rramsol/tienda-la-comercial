# -*- coding: utf-8 -*-
# Programa de comisiones del mes - La Comercial
# Refactorizado: nombres descriptivos, constantes con nombre y sin código muerto.

# Umbral de ventas a partir del cual aplica la comisión alta
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05

# Umbral de ventas a partir del cual se otorga bono adicional
UMBRAL_BONO = 50000
MONTO_BONO = 500

# Lista de vendedores: cada tupla es (nombre, total_vendido_en_el_mes)
vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comisiones():
    total_a_pagar = 0

    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)

    for nombre, monto_vendido in vendedores:
        # Vendedores que superan el umbral reciben una tasa de comisión mayor,
        # y si además superan el umbral de bono, se les suma un monto fijo extra
        if monto_vendido > UMBRAL_COMISION_ALTA:
            comision = round(monto_vendido * TASA_COMISION_ALTA, 2)
            bono = MONTO_BONO if monto_vendido > UMBRAL_BONO else 0
        else:
            comision = round(monto_vendido * TASA_COMISION_BAJA, 2)
            bono = 0

        total_vendedor = round(comision + bono, 2)
        total_a_pagar = total_a_pagar + total_vendedor
        print(nombre + ": Q " + str(total_vendedor))

    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_a_pagar, 2)))


calcular_comisiones()
