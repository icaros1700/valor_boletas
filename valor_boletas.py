def calcular_precio_boletas(tipo_sala, cantidad_boletas, hora_pico, tarjeta_cinema, reserva):
    # Tarifas básicas
    tarifas = {'Dinamix': 18800, '3D': 15500, '2D': 11300}
    tarifa_base = tarifas[tipo_sala]
    
    # Incrementos por hora pico
    if hora_pico:
        if tipo_sala == 'Dinamix':
            tarifa_base *= 1.50
        elif tipo_sala in ['3D', '2D']:
            tarifa_base *= 1.25

    # Descuentos y recargos
    total_descuento = 0
    total_recargo = 0

    # Descuento por hora no pico
    if not hora_pico:
        total_descuento += 0.10 * tarifa_base
        if cantidad_boletas >= 3:
            total_descuento += 500

    # Descuento por tarjeta del cinema
    if tarjeta_cinema:
        total_descuento += 0.05 * tarifas[tipo_sala]

    # Recargo por reserva
    if reserva:
        total_recargo += 2000

    # Cálculo del precio final
    precio_por_boleta = tarifa_base - total_descuento + total_recargo
    precio_total = precio_por_boleta * cantidad_boletas

    return precio_total

# Ejemplo de uso
tipo_sala = '3D'
cantidad_boletas = 4
hora_pico = False
tarjeta_cinema = True
reserva = False

precio = calcular_precio_boletas(tipo_sala, cantidad_boletas, hora_pico, tarjeta_cinema, reserva)
print(f"El precio total de las boletas es: {precio} pesos")
