# -*- coding: utf-8 -*-
# Modulo de descuentos de La Comercial

DESCUENTO_CLIENTE_FRECUENTE = 0.08
UMBRAL_MAYOREO = 12
DESCUENTO_MAYOREO = 0.15

def descuento_cliente_frecuente(subtotal):
    return subtotal * DESCUENTO_CLIENTE_FRECUENTE

def descuento_por_volumen(cantidad, precio_unitario):
    if cantidad >= UMBRAL_MAYOREO:
        return precio_unitario * cantidad * DESCUENTO_MAYOREO
    return 0
