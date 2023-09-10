from src.ordenar_numeros import ordenar_numeros

# Teste para verificar se a função ordena corretamente uma lista vazia
def test_ordenar_numeros_lista_vazia():
    assert ordenar_numeros([]) == []

# Teste para verificar se a função ordena corretamente uma lista com um elemento
def test_ordenar_numeros_lista_com_um_elemento():
    assert ordenar_numeros([42]) == [42]

# Teste para verificar se a função ordena corretamente uma lista com elementos repetidos
def test_ordenar_numeros_lista_com_elementos_repetidos():
    assert ordenar_numeros([3, 1, 2, 3, 2, 1]) == [1, 1, 2, 2, 3, 3]

# Teste para verificar se a função ordena corretamente uma lista em ordem decrescente
def test_ordenar_numeros_lista_em_ordem_decrescente():
    assert ordenar_numeros([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

# Teste para verificar se a função ordena corretamente uma lista em ordem crescente
def test_ordenar_numeros_lista_em_ordem_crescente():
    assert ordenar_numeros([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Teste para verificar se a função ordena corretamente uma lista com números negativos
def test_ordenar_numeros_lista_com_numeros_negativos():
    assert ordenar_numeros([-5, -2, 0, -3, -1]) == [-5, -3, -2, -1, 0]

# Teste para verificar se a função ordena corretamente uma lista mista de números
def test_ordenar_numeros_lista_mista():
    assert ordenar_numeros([10, -5, 7, 0, 3, -2]) == [-5, -2, 0, 3, 7, 10]

# Teste para verificar se a função ordena corretamente uma lista mista de números flutuantes
def test_ordenar_numeros_flutuantes():
    assert ordenar_numeros([10.5, -5.75, 7.02, 0, 3.25, -2.34]) == [-5.75, -2.34, 0, 3.25, 7.02, 10.5]

# Teste para verificar se a função mantém a lista original inalterada
def test_ordenar_numeros_lista_original_inalterada():
    lista = [3, 1, 2]
    ordenar_numeros(lista)
    assert lista == [3, 1, 2]