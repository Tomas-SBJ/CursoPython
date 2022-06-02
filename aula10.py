"""
Condições 

IF
ELIF
ELSE

Operadores Relacionais

== Igualdade 
> Maior que
>= Maior ou igual a
< Menor que 
<= Menor ou igual a 
!= Diferente
"""

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar empréstimo
muitoJovem = 18 # Muito jovem para pegar o empréstimo
muitoVelho = 30 # Muito velho para pegar o empréstimo

if idade >= muitoJovem and idade <= muitoVelho:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')
