"""
    Programa simples que inverte uma palavra e verifica se ela é um PALÍNDROMO, uma palavra que pode ser lida de trás para frente, assim como da frente para trás. Para isso, usaremos uma estrutura de pilha baseada em uma lista do python.
"""
palavra = input('Digite uma palavra para ser verificada: ')

pilha = [] #Lista vazia que será usada como pilha

# 1) Pega cada letra da palavra e insere no final (topo) da pilha
for letra in palavra:
    pilha.append(letra)
    print(pilha)

print('*'*50)

inverso = ""

#2) Vamos retirar as letras da pilha, uma a uma, DO FIM PARA O INÍCIO.
#A operação se repete enquanto a pilha não estiver vazia.
#Cada letra retirada é acrescentada à variável inverso.
while len(pilha)>0:
    letra = pilha.pop()     # Retira o último elemento da lista
    inverso += letra        # Acrescenta a letra ao inverso
    print(f"Pilha: {pilha}; inverso: {inverso}")
print("*"*50)

print("Palavra original: ", palavra)
print("Palavra invertida: ", inverso)

if palavra.lower() == inverso.lower():
    print(f"A palavra {palavra} é palíndroma")
else:
    print(f"A palavra {palavra} não é palíndroma")
