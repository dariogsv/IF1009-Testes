import main
import pytest
import math

# 1. Instale um framework de testes unitários de sua preferência (e.g., JUnit, TestNG, pytest, unittest). Cole, logo abaixo, a imagem do seu terminal mostrando a versão do framework de testes instalado.
# 2. Crie um caso de teste que passa e execute a suíte de testes. Qual foi o comando utilizado para executar a suíte de testes? Cole, logo abaixo, a imagem do seu terminal após a execução desse passo.
def test_sqrt_5_digits_precision():
    assert f"{main.sqrt(4):.5f}" == f"{math.sqrt(4):.5f}"
    assert f"{main.sqrt(8):.5f}" == f"{math.sqrt(8):.5f}"
    assert f"{main.sqrt(9):.5f}" == f"{math.sqrt(9):.5f}"
    assert f"{main.sqrt(15):.5f}" == f"{math.sqrt(15):.5f}"
# 3. Crie um caso de teste que falha e execute a suíte de testes. Qual foi o comando utilizado para executar a suíte de testes? Cole, logo abaixo, a imagem do seu terminal após a execução desse passo.
def test_sqrt_19_digits_precision():
    assert f"{main.sqrt(4):.19f}" == f"{math.sqrt(4):.19f}"
    assert f"{main.sqrt(8):.19f}" == f"{math.sqrt(8):.19f}"
    assert f"{main.sqrt(9):.19f}" == f"{math.sqrt(9):.19f}"
    assert f"{main.sqrt(15):.19f}" == f"{math.sqrt(15):.15f}"

# 4. Crie um caso de teste que passa apenas se uma exceção for lançada (e.g., divisão por zero). Cole, logo abaixo, as imagens do caso de teste criado e do seu terminal após a execução da suíte de testes.

def test_sqrt_negative_number():
    with pytest.raises(ValueError) as excinfo:
        main.sqrt(-4)
    assert str(excinfo.value) == "Cannot compute the square root of a negative number."

# 5. Crie um método que prepare o ambiente para a execução de um ou mais testes (setup). Cole, logo abaixo, as imagens do(s) método(s) criado(s) e do seu terminal após a execução da suíte de testes.
@pytest.fixture
def setup_and_teardown():
    main.PENDING = 0
    main.STORED = 2
    main.SALLED = 0
    # Tudo antes do yield é o setup
    yield
    # Tudo depois do yield é o teardown
    main.PENDING = 0
    main.STORED = 0
    main.SALLED = 0

def test_buy(setup_and_teardown): # Adicionado o fixture como argumento
    with pytest.raises(Exception) as excinfo:
        main.buy(3)
    assert str(excinfo.value) == "No items in storage"

# 6. Crie um método que restaura o ambiente após a execução de um ou mais testes (teardown). Cole, logo abaixo, as imagens do(s) método(s) criado(s) e do seu terminal após a execução da suíte de testes.
# (Este item já foi abordado pela fixture setup_and_teardown acima)

# 7. Execute a suíte de testes ignorando um ou mais casos de teste. Qual foi o comando utilizado? Cole, logo abaixo, a imagem do seu terminal após a execução desse passo.
# Comando: pytest -k "not test_sqrt_19_digits_precision"
# (Não é possível colar a imagem do terminal)

# 8. Escolha uma funcionalidade suportada pelo framework de testes que você considera interessante. Descreva, a seguir, a funcionalidade e em quais cenários ela é útil. Cole, logo abaixo, a imagem do seu terminal após a execução do comando para a funcionalidade que foi escolhida."
@pytest.mark.parametrize("input_num, expected_output", [
    (4, 2.0),
    (9, 3.0),
    (16, 4.0),
    (0, 0.0),
    (1, 1.0),
])
def test_sqrt_parametrized(input_num, expected_output):
    assert main.sqrt(input_num) == expected_output