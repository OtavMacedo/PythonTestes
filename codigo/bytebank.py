from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split("/")
        ano_atual = date.today().year
        return ano_atual - int(data_nascimento_quebrada[-1])

    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebrado = nome_completo.split()
        return nome_quebrado[-1]

    def eh_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self._salario == 100000 and self.sobrenome() in sobrenomes

    def descrescimo_salario(self):
        if self.eh_socio():
            descrescimo = self._salario * 0.1
            self._salario = self._salario - descrescimo

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception("O salário é muito alto para receber bônus")
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'