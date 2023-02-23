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

#TESTES

resultado = busca_sequencial(nomes_desord,"GABRIEL")

print(f"Posição do nome GABRIEL: {resultado}")


