import rpyc
import sys
import os
from random import randint

def criarVetor():
	# cria lista vazia
	vetor = []
	# aguarda o input do cliente do tamanho do vetor
	tamanho_vetor = int(input("Insira o tamanho do vetor: "))
	
	# adiciona na lista um valor variando de 0 até tamanho_vetor -1
	for i in range(tamanho_vetor):
		vetor.append(randint(0, tamanho_vetor -1))
	# retorna vetor preenchido
	return vetor

if len(sys.argv) < 2:
  exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
conn = rpyc.connect(server,18861)
print(conn.root)
print(conn.root.get_answer())
print(conn.root.the_real_answer_though)
# chama função para criar o vetor
vetor_cliente = criarVetor()
# executa o método exposto do servidor para fazer a soma
soma_vetor = conn.root.exposed_somaVetor(vetor_cliente)