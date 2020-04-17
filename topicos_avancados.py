# -*- coding: utf-8 -*-
# Função enumerate

lista = ["avocato", "anana", "dióspero", "tangerina"]

print ("\n ENUMARATE")

for i, nome in enumerate(lista):
	print (i,nome)


# FILTER

print("\n FILTER")

def pares (i):
	if i % 2 ==0:
		return i


lista1 = [1,2,3,4,5,6,7,8,9,10]

lista_pares = filter(pares, lista1)
print (list(lista_pares))

# MAP

print ("\n MAP")

def dobro(x):
	return x*2

valor = [10,20,30,40,50]

valor_dobrado = list(map(dobro, valor))
print (valor_dobrado)


# ZIP, concatena duas listas


print ("\n ZIP")

listaa = [1,2,3,4,5]
listab = ["aaa","bbb","ccc","ddd","eee"]

for numero,nome in zip(listaa,listab):
	print (numero, nome)
