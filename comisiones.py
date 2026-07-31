# -*- coding: utf-8 -*-
# Calcula e imprime el reporte mensual de comisiones de La Comercial.
 
anchoReporte = 44
limitComisionAlta = 30000
tasaComisionAlta = 0.08
limitBono = 50000
montoBono = 500
tasaComisionBase = 0.05
decimalesMoneda = 2
 
# lista de vendedores
vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]

#Calcula la comisión y el bono correspondientes a un vendedor.
def calcularTotalVendedor(ventasMensuales):
    
    # Las ventas superiores al límite reciben la tasa de comisión alta.
    if ventasMensuales > limitComisionAlta:
        tasaComision = tasaComisionAlta
    
    # Las ventas iguales o inferiores al límite reciben la tasa base.
    else:
        tasaComision = tasaComisionBase

    # Calcula la comisión y el bono, redondeando a los decimales de moneda.
    comision = ventasMensuales * tasaComision
    comision = round(comision, decimalesMoneda)

    # Si las ventas superan el límite de bono, se otorga el bono.
    if ventasMensuales > limitBono:
        bono = montoBono
        
    # Si las ventas no superan el límite de bono, no se otorga bono.
    else:
        bono = 0

    return round(comision + bono, decimalesMoneda)

# Devuelve las comisiones individuales y el total mensual
def calcular_comisiones():
    resultados = []
    totalPagar = 0
    
    # Se recorre la lista de vendedores y se calcula la comisión y el bono de cada uno.
    for nombreVendedor, ventasMensuales in vendedores:
        totalVendedor = calcularTotalVendedor(ventasMensuales)
        resultados.append((nombreVendedor, totalVendedor))
        totalPagar = totalPagar + totalVendedor

    return resultados, totalPagar

# Imprime el reporte conservando su formato original
def imprimir_reporte(resultados, totalPagar):
    print("=" * anchoReporte)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * anchoReporte)

    # Se recorre la lista de resultados y se imprime el nombre del vendedor y su comisión total.
    for nombreVendedor, totalVendedor in resultados:
        print(nombreVendedor + ": Q " + str(totalVendedor))

    # ta = tp * 1.12
    # print("con iva", ta)
    print("-" * anchoReporte)
    print(
        "Total a pagar: Q "
        + str(round(totalPagar, decimalesMoneda))
    )


resultados, totalPagar = calcular_comisiones()
imprimir_reporte(resultados, totalPagar)