"""
  ALGORITMO DE BUSCA BINÁRIA
  Dados uma lista, que deve estar PREVIAMENTE ORDENADA,
  e um valor de busca, divide a lista em duas metades
  procurando pelo valor de busca apenas na metade onde
  o valor poderia estar. Novas subdivisões são feitas
  até que se encontre o valor de busca ou que reste
  apenas uma sublista vazia, quando então se conclui
  que o valor de busca não existe na lista.
"""
comps = 0       # Conta o número de comparações
def busca_binaria(lista, val):
    global comps
    comps = 0
    ini = 0               # Início da lista
    fim = len(lista) - 1  # Fim da lista

    while ini <= fim:
        meio = (ini + fim) // 2     # Divisão inteira

        # O valor de busca foi encotrado.
        # Retorna a posição
        if lista[meio] == val: 
            comps += 1
            return meio

        elif val < lista[meio]:
            comps += 2
            fim = meio - 1

        else: # val > lista[meio]
            comps += 2
            ini = meio + 1

    return -1   # valor não existe na lista
from data.nomes_desord import nomes as nomes_desord

# TESTES COM NOMES

import sys
sys.dont_write_bytecode = True      # Impede a criação do cache

from time import time

from data.lista_nomes import nomes

# Busca pelo nome GABRIEL
hora_ini = time()
resultado = busca_binaria(nomes, "GABRIEL")
hora_fim = time()
print(f"Posição do nome GABRIEL na lista: {resultado}, Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

# Busca pelo nome CARLOS
hora_ini = time()
resultado = busca_binaria(nomes, "CARLOS")
hora_fim = time()
print(f"Posição do nome CARLOS na lista: {resultado}, Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

# Busca pelo nome YARA
hora_ini = time()
resultado = busca_binaria(nomes, "YARA")
hora_fim = time()
print(f"Posição do nome YARA na lista: {resultado}, Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")

# Busca pelo nome ORKUTILSON
hora_ini = time()
resultado = busca_binaria(nomes, "ORKUTILSON")
hora_fim = time()
print(f"Posição do nome ORKUTILSON na lista: {resultado}, Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")




