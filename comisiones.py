# -*- coding: utf-8 -*-
"""
Módulo de cálculo de comisiones de La Comercial.

Aplica las reglas de negocio para calcular el pago mensual
de los vendedores según sus ventas:
- Ventas superiores al límite establecido reciben comisión alta.
- Ventas superiores al límite del bono reciben un incentivo adicional.
- El resto recibe la comisión base.
"""

COMISION_ALTA = 0.08
COMISION_BASE = 0.05

VENTAS_MINIMAS_COMISION_ALTA = 30000
VENTAS_MINIMAS_BONO = 50000

BONO_ALTO_VENDEDOR = 500


VENDEDORES = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comision(monto_ventas):
    """
    Calcula la comisión correspondiente al vendedor
    según el monto total vendido.
    """
    if monto_ventas > VENTAS_MINIMAS_COMISION_ALTA:
        return monto_ventas * COMISION_ALTA

    return monto_ventas * COMISION_BASE


def calcular_bono(monto_ventas):
    """
    Aplica el bono adicional cuando las ventas alcanzan
    el nivel establecido por la regla de negocio.
    """
    if monto_ventas > VENTAS_MINIMAS_BONO:
        return BONO_ALTO_VENDEDOR

    return 0


def calcular_total_vendedor(monto_ventas):
    """
    Obtiene el pago total del vendedor sumando comisión y bono.
    """
    comision = calcular_comision(monto_ventas)
    bono = calcular_bono(monto_ventas)

    return round(comision + bono, 2)


def calcular_comisiones(vendedores):
    """
    Procesa la lista de vendedores y devuelve los resultados
    individuales junto con el total general de comisiones.
    """
    resultados = []
    total_comisiones = 0

    for nombre, ventas in vendedores:
        total_vendedor = calcular_total_vendedor(ventas)

        total_comisiones += total_vendedor

        resultados.append(
            (nombre, total_vendedor)
        )

    return resultados, total_comisiones


def imprimir_reporte(resultados, total_comisiones):
    """
    Presenta el reporte final de comisiones manteniendo
    el formato original del sistema.
    """
    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)

    for nombre, total in resultados:
        print(nombre + ": Q " + str(total))

    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_comisiones, 2)))


def main():
    resultados, total_comisiones = calcular_comisiones(VENDEDORES)

    imprimir_reporte(
        resultados,
        total_comisiones
    )


main()