import pytest
from pytest import mark
from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        #Given-Contexto
        entrada = '13/03/2000'
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1000)

        #When-Ação
        resultado = funcionario_teste.idade()

        #Then-Desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Bruno_Andrade_deve_retornar_Andrade(self):
        entrada = ' Bruno Andrade    '
        esperado = 'Andrade'

        bruno = Funcionario(entrada, '17/09/1999', 1000)

        resultado = bruno.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_nome = "Paulo José"
        entrada_salario = 100000
        
        esperado = 90000

        funcionario = Funcionario(entrada_nome, '17/09/1999', entrada_salario)
        funcionario.decrescimo_salario()

        resultado = funcionario.salario

        assert resultado == esperado

    @mark.calcular_bonus #pytest -m calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        
        esperado = 100

        funcionario = Funcionario('teste', '17/09/1999', entrada)
        resultado = funcionario.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus #pytest -m calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000
            
            funcionario = Funcionario('teste', '17/09/1999', entrada)
            resultado = funcionario.calcular_bonus()

            assert resultado