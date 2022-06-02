"""
Entrada de dados
"""

nome = input("Qual o seu nome ?")
idade = input("Qual a sua idade ?")

anoNascimento = 2022 - int(idade)

print(f'{nome} tem {idade} anos de idade e nasceu no ano de {anoNascimento}.')