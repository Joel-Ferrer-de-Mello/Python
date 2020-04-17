# -*- coding: utf-8 -*-
"""
Aula sobre ARQUIVOS
Autor: Joel Ferrer de Mello

FUNÇÕES:
read () le o arquivo inteiro
readline () le uma linha do arquivo
readlines () le e armazena em uma linha

"""

arquivo = open ("arquivo.txt", "w")
arquivo.write ("Modo r abre arquivo somente leitura.\n")
arquivo.write ("Modo w abre arquivo para escrita, caso já exista será apagado e um novo arquivo vazio será criado.\n")
arquivo.write ("Modo a abre arquivo para leitura e escrita, adiciona o novo conteúdo ao fim do arquivo.\n")
arquivo.write ("Modo r+ abre arquivo para leitura e escrita.\n")
arquivo.write ("Modo w+ abre arquivo para escrita, também apagada o conteúdo do arquivo anterior.\n")
arquivo.write ("Modo a+ abre arquivo para leitura e escrita (atualização).\n")
arquivo.close() #sempre que abrir precisará fechar ao final


arquivo = open ("arquivo.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

for linha in linhas:
	print (linha)

