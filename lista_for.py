# -*- coding: utf-8 -*-
lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = ["joel", "tais", "miguel", "laura"]
lista3 = [1,2,3,4,True,False,"joel","tais","miguel","laura"]

lista3.append ("Vovô Chico") #inserir mais item na lista
lista3.append ("Vovó Elaine")

print (lista3.index("joel")) # qual a posicao da variavel dentro da lista

print (lista3.count(4)) # contar um item na lista
lista3.append (4)
print (lista3.count(4)) # contar um item na lista
lista3.remove(4) # remove o item 4 da lista PODE USAR O DEL também
lista3.reverse() # inverte a lista
lista1.sort()   # ordena a lista

for i in lista3:
	print (i)
