# 1. Función para aplicar descuentos y promociones
def calcular_total(precio_unitario, cantidad):
    if cantidad < 0 or precio_unitario < 0:
        raise ValueError("Cantidad y precio deben ser positivos")
    
    total = precio_unitario * cantidad
    # Promoción: 20% de descuento si compra entre 5 y 10 unidades
    if 5 <= cantidad <= 10:
        total = total * 0.8
    return total

# 2. Función para simular métodos de pago
def procesar_pago(metodo, monto):
    metodos_validos = ["tarjeta", "paypal", "efectivo"]
    if metodo.lower() not in metodos_validos:
        raise ValueError(f"Error: Método de pago '{metodo}' no es válido.")
    
    if monto <= 0:
        raise ValueError("Error: El monto a pagar debe ser mayor a 0.")
    
    return f"Pago de ${monto} procesado exitosamente con {metodo.lower()}."

# 3. Función para detectar errores en generación de facturas
def generar_factura(datos_compra):
    if "cliente" not in datos_compra or not datos_compra["cliente"]:
        raise ValueError("Error en factura: Falta el nombre del cliente.")
    
    if "monto" not in datos_compra or datos_compra["monto"] <= 0:
        raise ValueError("Error en factura: Monto inválido o faltante.")
        
    return f"Factura generada: Cliente {datos_compra['cliente']}, Total: ${datos_compra['monto']}"



    