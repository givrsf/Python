'''--------------------------------------------------------------------------------------------
UNIVERSIDADE PAULISTA - ENG COMPUTAÇÃO - BACELAR
Nome: Gisele Veras Freitas
RA : N3882B-5
Turma : CP6P01
Lista: 01 - 05
Enunciado: 06 – Escreva o programa que receba o valor do salário, do aumento (%) e calcule o valor do novo salário.
Considere o salário de R$ 750,00 e o aumento de 15%.
--------------------------------------------------------------------------------------------'''
salarioatual = 750
reajustado = salarioatual + (salarioatual * 15 / 100) 
print('O antigo salário, de RS{:.2f}, teve um reajuste de 15% de aumento, e passa a valer R${:.2F}.'.format(salarioatual, reajustado))
