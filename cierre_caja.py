METODO_EFECTIVO = "EF"
METODO_TARJETA = "TJ"

TASA_IVA = 0.12
TASA_COMISION_POS = 0.05
ANCHO_REPORTE = 42

ventas_diarias = [
    (METODO_EFECTIVO, 150.00),
    (METODO_TARJETA, 89.50),
    (METODO_EFECTIVO, 45.25),
    (METODO_TARJETA, 210.00),
    (METODO_EFECTIVO, 78.00),
    (METODO_TARJETA, 156.75),
    (METODO_EFECTIVO, 92.50),
    (METODO_EFECTIVO, 34.00),
    (METODO_TARJETA, 67.25),
    (METODO_EFECTIVO, 125.00),
]


def calcular_totales_por_metodo(ventas):
    total_efectivo = 0.0
    total_tarjeta = 0.0

    for metodo_pago, monto_venta in ventas:
        if metodo_pago == METODO_EFECTIVO:
            total_efectivo += monto_venta
        elif metodo_pago == METODO_TARJETA:
            total_tarjeta += monto_venta
        else:
            raise ValueError(f"Metodo de pago no reconocido: {metodo_pago}")

    return total_efectivo, total_tarjeta


def calcular_iva_incluido(monto):
    return round(monto - (monto / (1 + TASA_IVA)), 2)


def calcular_comision_pos(total_tarjeta):
    return round(total_tarjeta * TASA_COMISION_POS, 2)


def mostrar_reporte_cierre(
    total_efectivo,
    total_tarjeta,
    iva_efectivo,
    iva_tarjeta,
    comision_pos,
):
    total_ventas = round(total_efectivo + total_tarjeta, 2)
    deposito_neto = round(total_ventas - comision_pos, 2)

    print("=" * ANCHO_REPORTE)
    print("      CIERRE DE CAJA - LA COMERCIAL")
    print("=" * ANCHO_REPORTE)
    print(f"Ventas en efectivo:      Q {total_efectivo:.2f}")
    print(f"IVA incluido (efectivo): Q {iva_efectivo:.2f}")
    print(f"Ventas con tarjeta:      Q {total_tarjeta:.2f}")
    print(f"IVA incluido (tarjeta):  Q {iva_tarjeta:.2f}")
    print(f"Comision del POS:        Q {comision_pos:.2f}")
    print("-" * ANCHO_REPORTE)
    print(f"Total del dia:           Q {total_ventas:.2f}")
    print(f"Deposito neto:           Q {deposito_neto:.2f}")


def ejecutar_cierre_caja():
    total_efectivo, total_tarjeta = calcular_totales_por_metodo(
        ventas_diarias
    )

    iva_efectivo = calcular_iva_incluido(total_efectivo)
    iva_tarjeta = calcular_iva_incluido(total_tarjeta)
    comision_pos = calcular_comision_pos(total_tarjeta)

    mostrar_reporte_cierre(
        total_efectivo,
        total_tarjeta,
        iva_efectivo,
        iva_tarjeta,
        comision_pos,
    )


if __name__ == "__main__":
    ejecutar_cierre_caja()