# -*- coding: utf-8 -*-
"""Programa para generar el cierre de caja diario."""

TASA_IVA = 0.12
TASA_COMISION_POS = 0.05

METODO_EFECTIVO = "EF"
METODO_TARJETA = "TJ"

VENTAS_DEL_DIA = [
    ("EF", 150.00),
    ("TJ", 89.50),
    ("EF", 45.25),
    ("TJ", 210.00),
    ("EF", 78.00),
    ("TJ", 156.75),
    ("EF", 92.50),
    ("EF", 34.00),
    ("TJ", 67.25),
    ("EF", 125.00),
]


def calcular_iva_incluido(total_venta):
    """Calcula el IVA del 12 % incluido en una venta."""

    subtotal_sin_iva = total_venta / (1 + TASA_IVA)
    iva_incluido = total_venta - subtotal_sin_iva

    return round(iva_incluido, 2)


def calcular_totales_por_metodo(ventas):
    """Suma las ventas en efectivo y con tarjeta."""

    total_efectivo = 0.0
    total_tarjeta = 0.0

    for metodo_pago, monto in ventas:
        if metodo_pago == METODO_EFECTIVO:
            total_efectivo += monto
        elif metodo_pago == METODO_TARJETA:
            total_tarjeta += monto
        else:
            print(
                "Método de pago no reconocido: "
                + str(metodo_pago)
            )

    return round(total_efectivo, 2), round(total_tarjeta, 2)


def generar_cierre_caja():
    """Calcula y muestra el cierre de caja del día."""

    total_efectivo, total_tarjeta = calcular_totales_por_metodo(
        VENTAS_DEL_DIA
    )

    iva_efectivo = calcular_iva_incluido(total_efectivo)
    iva_tarjeta = calcular_iva_incluido(total_tarjeta)

    comision_pos = round(
        total_tarjeta * TASA_COMISION_POS,
        2
    )

    total_dia = round(
        total_efectivo + total_tarjeta,
        2
    )

    deposito_neto = round(
        total_dia - comision_pos,
        2
    )

    print("=" * 42)
    print("CIERRE DE CAJA - LA COMERCIAL".center(42))
    print("=" * 42)
    print(f"Ventas en efectivo:      Q {total_efectivo:.2f}")
    print(f"IVA incluido (efectivo): Q {iva_efectivo:.2f}")
    print(f"Ventas con tarjeta:      Q {total_tarjeta:.2f}")
    print(f"IVA incluido (tarjeta):  Q {iva_tarjeta:.2f}")
    print(f"Comisión del POS:        Q {comision_pos:.2f}")
    print("-" * 42)
    print(f"Total del día:           Q {total_dia:.2f}")
    print(f"Depósito neto:           Q {deposito_neto:.2f}")


generar_cierre_caja()