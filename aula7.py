nome = 'Tomas'
idade = 19
altura = 1.77
maiorIdade = idade > 18
peso = 60

imc = peso / (altura * altura)

print(nome + ' tem ' + str(idade) + ' anos de idade e seu imc e ' + str(imc))

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{n} tem {i} anos de idade e se imc é {imc:.2f}'.format(n=nome, i=idade, imc=imc))