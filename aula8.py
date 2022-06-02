"""
* Criar variáveis para nome (str), idade (int)
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

"""
Printar = Tomás tem 19 anos, 1.77 de altura e pesa 60kg.
          Tomás nasceu em 2002
"""

nome = 'Tomas'
idade = 20
altura = 1.77
peso = 60.0
anoAtual = 2022
anoNascimento = anoAtual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {anoNascimento}')