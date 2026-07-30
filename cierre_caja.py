# -*- coding: utf-8 -*-
# programa de cierre de caja
# hecho por kevin
 
# lista de ventas del dia
# -*- coding: utf-8 -*-
# Programa de cierre de caja de La Comercial

# Constantes
IVA = 0.12
COMISION_POS = 0.05
ANCHO_REPORTE = 42

# Lista de ventas del día
ventas = [
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


def calcular_iva_incluido(monto):
    """Calcula el IVA incluido en un monto."""
    return round(monto - (monto / (1 + IVA)), 2)


def calcular_comision(monto):
    """Calcula la comisión por pagos con tarjeta."""
    return round(monto * COMISION_POS, 2)


def procesar_cierre_caja():
    total_efectivo = 0
    total_tarjeta = 0

    # Recorrer las ventas
    for tipo_pago, monto in ventas:
        if tipo_pago == "EF":
            total_efectivo += monto
        else:
            total_tarjeta += monto

    iva_efectivo = calcular_iva_incluido(total_efectivo)
    iva_tarjeta = calcular_iva_incluido(total_tarjeta)
    comision_pos = calcular_comision(total_tarjeta)

    total_dia = total_efectivo + total_tarjeta
    deposito_neto = total_dia - comision_pos

    print("=" * ANCHO_REPORTE)
    print("      CIERRE DE CAJA - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)
    print(f"Ventas en efectivo:      Q {total_efectivo:.2f}")
    print(f"IVA incluido (efectivo): Q {iva_efectivo:.2f}")
    print(f"Ventas con tarjeta:      Q {total_tarjeta:.2f}")
    print(f"IVA incluido (tarjeta):  Q {iva_tarjeta:.2f}")
    print(f"Comisión del POS:        Q {comision_pos:.2f}")
    print("-" * ANCHO_REPORTE)
    print(f"Total del día:           Q {total_dia:.2f}")
    print(f"Depósito neto:           Q {deposito_neto:.2f}")


if __name__ == "__main__":
    procesar_cierre_caja()