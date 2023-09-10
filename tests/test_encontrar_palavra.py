from src.encontrar_palavra import encontrar_palavra

# Teste para verificar se uma palavra está presente na frase
def test_encontrar_palavra_presente():
    assert encontrar_palavra("Isso é uma frase de exemplo", "frase") == True

# Teste para verificar se uma palavra não está presente na frase
def test_encontrar_palavra_ausente():
    assert encontrar_palavra("Esta é outra frase", "palavra") == False

# Teste para verificar se a função lida corretamente com letras maiúsculas e minúsculas
def test_encontrar_palavra_maiusculas_minusculas():
    assert encontrar_palavra("Python é uma linguagem de programação", "Python") == True

# Teste para verificar se a função lida corretamente com palavras compostas
def test_encontrar_palavra_palavra_composta():
    assert encontrar_palavra("Esta é uma palavra-composta", "palavra-composta") == True

# Teste para verificar se a função lida corretamente com palavras parciais
def test_encontrar_palavra_palavra_parcial():
    assert encontrar_palavra("Esta é uma palavra-parcialmente", "parcial") == False