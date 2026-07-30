# Metodos de pago disponibles
METODO_EFECTIVO = "EF"
METODO_TARJETA = "TJ"

# Valores utilizados en los calculos
PORCENTAJE_IVA = 0.12
PORCENTAJE_COMISION_POS = 0.05
DECIMALES_MONEDA = 2
ANCHO_REPORTE = 42

# Ventas registradas durante el dia
ventas_del_dia = [
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


def calcular_iva_incluido(total_ventas):
    # Obtiene solamente el IVA que ya se encuentra incluido
    total_sin_iva = total_ventas / (1 + PORCENTAJE_IVA)
    iva_incluido = total_ventas - total_sin_iva

    return round(iva_incluido, DECIMALES_MONEDA)


def generar_cierre_caja():
    # Acumuladores para separar las ventas por metodo de pago
    total_ventas_efectivo = 0
    total_ventas_tarjeta = 0

    # Recorre todas las ventas registradas
    for metodo_pago, monto_venta in ventas_del_dia:
        if metodo_pago == METODO_EFECTIVO:
            total_ventas_efectivo += monto_venta
        elif metodo_pago == METODO_TARJETA:
            total_ventas_tarjeta += monto_venta

    # Redondea los totales monetarios
    total_ventas_efectivo = round(
        total_ventas_efectivo,
        DECIMALES_MONEDA,
    )
    total_ventas_tarjeta = round(
        total_ventas_tarjeta,
        DECIMALES_MONEDA,
    )

    # Calcula el IVA incluido en cada tipo de venta
    iva_ventas_efectivo = calcular_iva_incluido(
        total_ventas_efectivo
    )
    iva_ventas_tarjeta = calcular_iva_incluido(
        total_ventas_tarjeta
    )

    # Calcula la comision cobrada por el servicio de POS
    comision_pos = round(
        total_ventas_tarjeta * PORCENTAJE_COMISION_POS,
        DECIMALES_MONEDA,
    )

    # Calcula los resultados generales del cierre
    total_ventas_dia = round(
        total_ventas_efectivo + total_ventas_tarjeta,
        DECIMALES_MONEDA,
    )
    deposito_neto = round(
        total_ventas_dia - comision_pos,
        DECIMALES_MONEDA,
    )

    # Muestra el reporte de cierre de caja
    print("=" * ANCHO_REPORTE)
    print("CIERRE DE CAJA - LA COMERCIAL".center(ANCHO_REPORTE))
    print("=" * ANCHO_REPORTE)
    print(
        f"Ventas en efectivo:      "
        f"Q {total_ventas_efectivo:.2f}"
    )
    print(
        f"IVA incluido (efectivo): "
        f"Q {iva_ventas_efectivo:.2f}"
    )
    print(
        f"Ventas con tarjeta:      "
        f"Q {total_ventas_tarjeta:.2f}"
    )
    print(
        f"IVA incluido (tarjeta):  "
        f"Q {iva_ventas_tarjeta:.2f}"
    )
    print(
        f"Comision del POS:        "
        f"Q {comision_pos:.2f}"
    )
    print("-" * ANCHO_REPORTE)
    print(
        f"Total del dia:           "
        f"Q {total_ventas_dia:.2f}"
    )
    print(
        f"Deposito neto:           "
        f"Q {deposito_neto:.2f}"
    )


generar_cierre_caja()