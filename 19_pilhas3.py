from lib.stack import Stack

# expr = "2+((5*(3/2+1)/4))"
expr = "(2+((5*(3-(2+1)/4))"

print(f"Expressão analisada: {expr}")

pilha = Stack()
#Percorre a expressão em busca de parênteses
for pos in range(len(expr)):
    #Empilha a posição quando é encontrado um abre parênteses
    if expr[pos] == "(":
        pilha.push(pos)
        print(pilha)

    # Desempilha a posição do último abre parênteses empilhado
    #quando um fecha parênteses é encontrado

    elif expr[pos] ==")":
        pos_abre = pilha.pop()
        print(f"Parêntese aberto na posição {pos_abre} foi fechado na posição {pos}")

while not pilha.is_empty():
    pos_abre = pilha.pop();
    print(f"ERRo: parentese aberto na posição {pos_abre} não possui o fecha correspondente")
