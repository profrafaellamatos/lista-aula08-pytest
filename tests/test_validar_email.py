from src.validar_email import validar_email

# Teste para verificar se um e-mail válido é reconhecido como válido
def test_validar_email_valido():
    assert validar_email("usuario@example.com") == True

# Teste para verificar se um e-mail inválido é reconhecido como inválido
def test_validar_email_invalido():
    assert validar_email("nao_e_um_email") == False

# Teste para verificar se um e-mail com formato inválido é reconhecido como inválido
def test_validar_email_formato_invalido():
    assert validar_email("usuario@exemplo") == False

# Teste para verificar se um e-mail com caracteres especiais é reconhecido como válido
def test_validar_email_caracteres_especiais():
    assert validar_email("us.er-123@example.com") == True

# Teste para verificar se um e-mail com subdomínio é reconhecido como válido
def test_validar_email_subdominio():
    assert validar_email("usuario@sub.exemplo.com") == True