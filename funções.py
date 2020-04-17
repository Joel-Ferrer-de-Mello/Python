# -*- coding: utf-8 -*-
"""
Aula sobre FUNÇÕES
Autor: Joel Ferrer de Mello

FUNÇÕES:
def

"""

def CALC (x, y, Operador):
	if Operador == "+":
	        return (x+y)
	elif Operador == "-":
	        return (x-y)
	elif Operador == "*":
	        return (x*y)
	elif Operador == "/":
	        return (x/y)
	else:
		return ("Operador digitado incorreto! Preste mais atenção da próxima vez...")
	


print (CALC (1041, 1089,"*"))
