# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

META_VENTAS = 30000.00
META_BONO = 50000.00
TASA_COMISION_ALTA = 0.08
TASA_COMISION_BAJA = 0.05
MONTO_BONO = 500

# lista de vendedores
vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]

def calcular_pago_vendedor(ventas_vendedor):
    # si vendio mas de 30000
    if ventas_vendedor > META_VENTAS:
        # calcula la comision del 8%
        tasa = TASA_COMISION_ALTA
    else:
        # calcula la comision del 5%
        tasa = TASA_COMISION_BAJA
        
    comision = round(ventas_vendedor * tasa, 2)
    
    # el bono es de 300
    if ventas_vendedor > META_BONO:
        bono = MONTO_BONO
    else:
        bono = 0
        
    return round(comision + bono, 2)

def calcular_comisiones(lista_vendedores):
    resultados = []
    total_comisiones = 0
    # recorre la lista
    for vendedor in lista_vendedores:
        nombre_vendedor = vendedor[0]
        ventas_vendedor = vendedor[1]
        
        total_vendedor = calcular_pago_vendedor(ventas_vendedor)
        total_comisiones = total_comisiones + total_vendedor
        
        resultados.append((nombre_vendedor, total_vendedor))
        
    return resultados, total_comisiones

def imprimir_reporte(resultados, total_comisiones):
    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)
    
    for nombre_vendedor, total_vendedor in resultados:
        print(nombre_vendedor + ": Q " + str(total_vendedor))
        
    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_comisiones, 2)))

resultados_finales, gran_total = calcular_comisiones(vendedores)
imprimir_reporte(resultados_finales, gran_total)