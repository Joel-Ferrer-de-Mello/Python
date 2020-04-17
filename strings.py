# -*- coding: utf-8 -*-
"""
Aula sobre STRINGS
Autor: Joel Ferrer de Mello
FUNÇÕES:
len (conta a quantidade de caracteres)
str (converte em string)
MÉTODOS:
lower converte para minúsculas
upper converte para maiúsculas
strip remove caracteres especiais
split converte em uma lista
find encontra caracteres dentro de uma string e retorna o início da posição, caso não encontre retornará -1
replace substitui uma palavra por outra

"""

nome1 = "Laura"
nome2 = "Miguel"

print (nome1 + " contém " + str(len(nome1)) + " caracteres")
print (nome2 + " contém " + str(len(nome2)) + " caracteres")

print (nome1[2:5]) # imprime do 3 caracter até o 5
print (nome2[0:3]) # imprime do 3 caracter até o 5

print (nome1.lower())
print (nome2.upper())

nome1 = nome1 + "   \n   "
print (nome1)
nome1 = nome1.strip()
print (nome1)
nome1 = nome1 + " Cotta de Mello de Mello"
print (nome1)
print (nome1.find("Cotta"))
nome1 = nome1.replace("Laura", "Miguel")
print (nome1)                  
nome1 = nome1.replace("Miguel", "Laura")
