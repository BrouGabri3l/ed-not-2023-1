
"""
Algoritmo de ordenação BUBBLE SORT
Percorre a lista a ser ordenada em sucessivas passadas,
trocando dois elementos adjacentes sempre que o segundo for MENOR que 
o primeiro. Efetua tantas passadas quanto necessárias, até que, na última passada,
nenhuma troca seja Efetuada
"""
arr = [6,4,9,0,2,5,8,3,1,7]
comps = trocas = passadas = 0
def bubble_sort(list):

    global comps,trocas,passadas 
    isSorted = False
    #Função bubble sort
    while((not isSorted)):
        #Enquanto nao estiver ordenada executa o que há nesse bloco
        hasChanges = False # variavel que vê se houve mudanças
        for pos in range(len(list)-1): # iteração percorrendo a lista até o penultimo elemento
            if(list[pos+1] < list[pos]):
                #se o valor da posição for maior que o valor da próxima posição
                #ele é invertido
                list[pos+1],list[pos] = list[pos], list[pos+1]
                hasChanges = True
                trocas+=1
            comps+=1
        passadas+=1
        if(not hasChanges):
            #se não houve mudanças retorna a lista e para a execução do loop while
            isSorted = True
            return list



print(f"Lista ordenada: {bubble_sort(arr)}, quantidade de passadas: {passadas}, quantidade de mudanças: {trocas}, quantidade de comparações: {comps}")