import pytest
from ecommerce import calcular_total, procesar_pago, generar_factura

# --- Pruebas: Descuentos y Promociones ---
def test_sin_descuento():
    assert calcular_total(100, 4) == 400

def test_con_descuento_promocion():
    assert calcular_total(100, 5) == 400  # 500 - 20% = 400

def test_descuento_valores_invalidos():
    with pytest.raises(ValueError):
        calcular_total(-10, 5)

# --- Pruebas: Métodos de Pago ---
def test_pago_valido_tarjeta():
    resultado = procesar_pago("tarjeta", 400)
    assert resultado == "Pago de $400 procesado exitosamente con tarjeta."

def test_pago_metodo_invalido():
    with pytest.raises(ValueError, match="no es válido"):
        procesar_pago("criptomoneda", 400)

def test_pago_monto_cero():
    with pytest.raises(ValueError, match="mayor a 0"):
        procesar_pago("paypal", 0)

# --- Pruebas: Generación de Facturas ---
def test_factura_exitosa():
    datos = {"cliente": "Alberto Marquina", "monto": 400}
    resultado = generar_factura(datos)
    assert resultado == "Factura generada: Cliente Alberto Marquina, Total: $400"

def test_factura_sin_cliente():
    datos = {"monto": 400}  # Falta el cliente
    with pytest.raises(ValueError, match="Falta el nombre del cliente"):
        generar_factura(datos)

def test_factura_monto_invalido():
    datos = {"cliente": "Alberto Marquina", "monto": -50}
    with pytest.raises(ValueError, match="Monto inválido o faltante"):
        generar_factura(datos)


