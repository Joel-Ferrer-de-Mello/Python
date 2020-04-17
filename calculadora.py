# -*- coding: utf-8 -*-
"""
Calculadora
Autor: Joel Ferrer de Mello
Função: fazer cálculos matemáticos (adição, subtração, divisão e multiplicação)
"""
print ("----------- Calculadora 1.0 -----------")

sair = False

while sair == False:

	num1 = input ("Digite o primeiro número: ")
	num1= int(num1)

	operador = input ("Digite o operador ( + - * / ): ")

	num2 = input ("Digite o segundo número: ")
	num2= int(num2)

	if operador == "+":
	        operador = "O resultado da operação " + str (num1) + " " + operador + " " + str (num2) + " é " + str(num1 + num2)
	elif operador == "-":
	        operador = "O resultado da operação " + str (num1) + " " + operador + " " + str (num2) + " é " + str(num1 - num2)
	elif operador == "*":
	        operador = "O resultado da operação " + str (num1) + " " + operador + " " + str (num2) + " é " + str(num1 * num2)
	elif operador == "/":
	        operador = "O resultado da operação " + str (num1) + " " + operador + " " + str (num2) + " é " + str(num1 / num2)
	else:
		operador = "Operador digitado incorreto! Preste mais atenção da próxima vez..."
	print (operador)

	continua = input ("Deseja continuar (s/n)? ")
	if continua == "n":
		sair = True
		
