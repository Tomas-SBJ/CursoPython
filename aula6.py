'''
 Iniciar com letra, pode conter números, separar _, letras minúsculas
'''

nome = 'Tomas'
idade = 19
altura = 1.77
maiorIdade = idade > 18
peso = 60

imc = peso / (altura * altura)

print(nome + ' tem ' + str(idade) + ' anos de idade e seu imc e ' + str(imc))

print('Nome', type(nome))
print('Idade', type(idade))
print('Altura', type(altura))
print('Maior de idade', type(maiorIdade))

print(altura * idade)