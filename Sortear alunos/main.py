#entrada de dados
import random
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')
lista = [a, b, c, d]

#processamento
escolhido = random.choice(lista)
print('O aluno que deverá apagar o quadro é o {}!'.format(escolhido))

#fim