"""
Módulo para el cálculo de comisiones mensuales de los vendedores de La Comercial.
Aplica diferentes tasas de comisión y bonos basados en metas de venta.
"""

META_VENTAS = 30000.00
META_BONO = 50000.00
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

def calcular_pago_vendedor(ventas_vendedor):
    """Calcula la comisión y el bono de un vendedor basado en sus ventas."""
    if ventas_vendedor > META_VENTAS:
        tasa = TASA_COMISION_ALTA
    else:
        tasa = TASA_COMISION_BAJA
        
    comision = round(ventas_vendedor * tasa, 2)
    
    # El bono se otorga únicamente si el vendedor supera la meta máxima
    if ventas_vendedor > META_BONO:
        bono = MONTO_BONO
    else:
        bono = 0
        
    return round(comision + bono, 2)

def calcular_comisiones(lista_vendedores):
    """Procesa las ventas y devuelve los resultados individuales y el total general."""
    resultados = []
    total_comisiones = 0
    
    for vendedor in lista_vendedores:
        nombre_vendedor = vendedor[0]
        ventas_vendedor = vendedor[1]
        
        total_vendedor = calcular_pago_vendedor(ventas_vendedor)
        total_comisiones = total_comisiones + total_vendedor
        
        resultados.append((nombre_vendedor, total_vendedor))
        
    return resultados, total_comisiones

def imprimir_reporte(resultados, total_comisiones):
    """Imprime el reporte detallado de comisiones."""
    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)
    
    for nombre_vendedor, total_vendedor in resultados:
        print(nombre_vendedor + ": Q " + str(total_vendedor))
        
    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_comisiones, 2)))

resultados_finales, gran_total = calcular_comisiones(vendedores)
imprimir_reporte(resultados_finales, gran_total)