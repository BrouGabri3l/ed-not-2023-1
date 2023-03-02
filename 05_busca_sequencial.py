from data.nomes_desord import nomes as nomes_desord
nums = [9,21,33,12,0,18,24,30,15,6,3,27]
'''
Função que realiza uma busca sequencial em uma lista procurando por val
se val for encontrado retorna a posição de val
caso contrario retorna -1
'''
def busca_sequencial(lista,val):
    #percorre a lista
    for pos in range(len(lista)):
        #verifica se houver valor, retorna a posição
        if val ==lista[pos]: return pos
    #se percorrer toda a lista e nao encontrar retorna -1
    return -1
##########################
# TESTES

# Procurando o valor 15
resultado = busca_sequencial(nums, 15)
print(f"Posição do valor 15 na lista: {resultado}")

# Procurando o valor 20
resultado = busca_sequencial(nums, 20)
print(f"Posição do valor 20 na lista: {resultado}")

# Procurando o valor 33
resultado = busca_sequencial(nums, 33)
print(f"Posição do valor 33 na lista: {resultado}")

# TESTES COM NOMES

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from time import time

from data.lista_nomes import nomes

# Busca pelo nome GABRIEL
hora_ini = time()
resultado = busca_sequencial(nomes, "GABRIEL")
hora_fim = time()
print(f"Posição do nome GABRIEL na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

# Busca pelo nome CARLOS
hora_ini = time()
resultado = busca_sequencial(nomes, "CARLOS")
hora_fim = time()
print(f"Posição do nome CARLOS na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

# Busca pelo nome YARA
hora_ini = time()
resultado = busca_sequencial(nomes, "YARA")
hora_fim = time()
print(f"Posição do nome YARA na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

# Busca pelo nome ORKUTILSON
hora_ini = time()
resultado = busca_sequencial(nomes, "ORKUTILSON")
hora_fim = time()
print(f"Posição do nome ORKUTILSON na lista: {resultado}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")


