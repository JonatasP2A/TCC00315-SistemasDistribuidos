import rpyc
import sys
import os
import time
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


if __name__ == "__main__":
   if len(sys.argv) != 2:
       print("Usage: {} SERVER".format(sys.argv[0]))
       sys.exit(1)
   server = sys.argv[1]
   conn = rpyc.connect('192.168.0.200', 18861)
   print(conn.root)
   print(conn.root.get_answer())
   print(conn.root.the_real_answer_though)
  
   # chama função para criar o vetor
   start = time.time()
   vetor_cliente = criarVetor()
   # executa o método exposto do servidor para fazer a soma
  
   soma_vetor = conn.root.exposed_somaVetor(vetor_cliente)
   end = time.time()
   print(f"O tempo para execução da função no cliente foi de: {end-start} \n")
   # Printa no terminal o valor da soma calculado pelo servidor
   print(f"A soma, calculada pelo Servidor, dos elementos do vetor é: {soma_vetor} \n")