import pytest
from pytest import mark

from codigo.bytebank import Funcionario


class TestClass:

    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2002'  # Given-Contexto
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_nome_recebe_Otavio_Augusto_deve_retornar_Augusto(self):
        entrada = "Otavio Augusto"
        esperado = "Augusto"

        otavio = Funcionario(entrada,"10/02/2004", 1111)
        resultado = otavio.sobrenome()

        assert resultado == esperado

    # @mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):

        # SE TEM O SOBRENOME DE UM SOCIO E RECEBE O SALARIO DE 100000
        entrada_salario = 100000 #GIVEN
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "10/02/2004", entrada_salario)
        funcionario_teste.descrescimo_salario() #WHEN

        resultado = funcionario_teste.salario

        assert esperado == resultado #THEN

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario_1000 = 1000

        esperado = 100

        funcionario_teste = Funcionario("teste", "10/02/2004", entrada_salario_1000)

        resultado = funcionario_teste.calcular_bonus()

        assert esperado == resultado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_valor_maior_que_10000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario_maior_que_10000 = 10001 #GIVEN

            funcionario_teste = Funcionario("Teste", "13/10/1991", entrada_salario_maior_que_10000)

            resultado = funcionario_teste.calcular_bonus() #WHEN

            assert resultado #THEN

    def test_quando_nome_eh_otavio_property_nome_deve_retornar_otavio(self):
        nome = "Otavio"

        otavio = Funcionario(nome, "13/10/2000", 10000)

        esperado = "Otavio"

        resultado = otavio.nome

        assert resultado == esperado