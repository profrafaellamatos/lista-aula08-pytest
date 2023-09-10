from src.converter_temp_f_para_c import converter_temp_f_para_c

def test_converter_fahrenheit_para_celsius_ponto_de_congelamento():
    assert converter_temp_f_para_c(32) == 0

# Teste para verificar se 212°F é igual a 100°C (ponto de ebulição da água)
def test_converter_fahrenheit_para_celsius_ponto_de_ebulicao():
    assert converter_temp_f_para_c(212) == 100

# Teste para verificar se 0°F é igual a -17.7778°C (teste de valor negativo)
def test_converter_fahrenheit_para_celsius_valor_negativo():
    resultado = converter_temp_f_para_c(0)
    assert round(resultado, 2) == -17.78

# Teste para verificar se -40°F é igual a -40°C (temperatura igual em ambas as escalas)
def test_converter_fahrenheit_para_celsius_temperatura_igual():
    assert converter_temp_f_para_c(-40) == -40

# Teste para verificar se a função lida corretamente com valores decimais
def test_converter_fahrenheit_para_celsius_valores_decimais():
    assert converter_temp_f_para_c(98.6) == 37