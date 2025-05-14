from main import sqrt, buy
import main
import pytest
import math

# 1. Instale um framework de testes unitários de sua preferência (e.g., JUnit, TestNG, pytest, unittest). Cole, logo abaixo, a imagem do seu terminal mostrando a versão do framework de testes instalado.
# 2. Crie um caso de teste que passa e execute a suíte de testes. Qual foi o comando utilizado para executar a suíte de testes? Cole, logo abaixo, a imagem do seu terminal após a execução desse passo.
def test_sqrt_5_digits_precision():
    assert f"{sqrt(4):.5f}" == f"{math.sqrt(4):.5f}"
    assert f"{sqrt(8):.5f}" == f"{math.sqrt(8):.5f}"
    assert f"{sqrt(9):.5f}" == f"{math.sqrt(9):.5f}"
    assert f"{sqrt(15):.5f}" == f"{math.sqrt(15):.5f}"
# 3. Crie um caso de teste que falha e execute a suíte de testes. Qual foi o comando utilizado para executar a suíte de testes? Cole, logo abaixo, a imagem do seu terminal após a execução desse passo.
def test_sqrt_19_digits_precision():
    assert f"{sqrt(4):.19f}" == f"{math.sqrt(4):.19f}"
    assert f"{sqrt(8):.19f}" == f"{math.sqrt(8):.19f}"
    assert f"{sqrt(9):.19f}" == f"{math.sqrt(9):.19f}"
    assert f"{sqrt(15):.19f}" == f"{math.sqrt(15):.15f}"

# 4. Crie um caso de teste que passa apenas se uma exceção for lançada (e.g., divisão por zero). Cole, logo abaixo, as imagens do caso de teste criado e do seu terminal após a execução da suíte de testes.

def test_sqrt_negative_number():
    with pytest.raises(ValueError) as excinfo:
        sqrt(-4)
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

def test_buy():
    with pytest.raises(ValueError) as excinfo:
        buy(3)
    assert str(excinfo.value) == f"Only {main.STORED} items in stock, but {3} requested."
# 6. Crie um método que restaura o ambiente após a execução de um ou mais testes (teardown). Cole, logo abaixo, as imagens do(s) método(s) criado(s) e do seu terminal após a execução da suíte de testes.
# 7. Execute a suíte de testes ignorando um ou mais casos de teste. Qual foi o comando utilizado? Cole, logo abaixo, a imagem do seu terminal após a execução desse passo.
# 8. Escolha uma funcionalidade suportada pelo framework de testes que você considera interessante. Descreva, a seguir, a funcionalidade e em quais cenários ela é útil. Cole, logo abaixo, a imagem do seu terminal após a execução do comando para a funcionalidade que foi escolhida.
