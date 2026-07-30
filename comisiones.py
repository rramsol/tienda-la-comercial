# -*- coding: utf-8 -*-
"""Cálculo de comisiones mensuales de vendedores - La Comercial."""

# Vendedores que superan este umbral de ventas reciben la tasa alta de comisión
UMBRAL_COMISION_ALTA = 30000
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05

# Además de la comisión alta, quien supere este umbral recibe un bono fijo
UMBRAL_BONO = 50000
MONTO_BONO = 500

# Lista de vendedores: cada tupla contiene (nombre, total_vendido_en_el_mes)
vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comisiones():
    """Calcula la comisión, bono y total a pagar de cada vendedor.

    Devuelve la lista de resultados por vendedor y el total general,
    sin imprimir nada: el cálculo no debe saber cómo se muestra.
    """
    # Aquí se almacenan los resultados individuales de cada vendedor
    resultados = []

    # Acumula el total de comisiones y bonos que pagará la empresa
    total_a_pagar = 0

    # Se procesa cada vendedor de la lista
    for nombre, monto_vendido in vendedores:

        # Si supera el umbral, obtiene la comisión alta
        if monto_vendido > UMBRAL_COMISION_ALTA:
            comision = round(monto_vendido * TASA_COMISION_ALTA, 2)

            # El bono solo aplica si supera el umbral establecido
            bono = MONTO_BONO if monto_vendido > UMBRAL_BONO else 0
        else:
            # En caso contrario recibe la comisión estándar
            comision = round(monto_vendido * TASA_COMISION_BAJA, 2)
            bono = 0

        # Suma la comisión y el bono para obtener el pago final del vendedor
        total_vendedor = round(comision + bono, 2)

        # Acumula el total general a pagar
        total_a_pagar = total_a_pagar + total_vendedor

        # Guarda el nombre del vendedor junto con el total que recibirá
        resultados.append((nombre, total_vendedor))

    # Devuelve los resultados y el total general redondeado a dos decimales
    return resultados, round(total_a_pagar, 2)


def imprimir_reporte(resultados, total_a_pagar):
    """Imprime el reporte de comisiones del mes en el formato de la tienda."""

    # Encabezado del reporte
    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)

    # Muestra el total correspondiente a cada vendedor
    for nombre, total_vendedor in resultados:
        print(nombre + ": Q " + str(total_vendedor))

    # Muestra el total general de pagos
    print("-" * 44)
    print("Total a pagar: Q " + str(total_a_pagar))


# Primero se calculan las comisiones
resultados, total_a_pagar = calcular_comisiones()

# Luego se imprime el reporte con la información obtenida
imprimir_reporte(resultados, total_a_pagar)