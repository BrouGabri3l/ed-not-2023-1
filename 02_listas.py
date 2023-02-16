"""
Listas podem receber diversos tipos de dados
"""
valores = [2,3,5,7,9,11,"batata","tomate",True]
"""
Operações sobre listas
1)Percurso: percorre a lista do primeiro ao ultimo elemento
"""
for v in valores:
    print(v)

print("*"*80)
#2) inserção de novos elementos no final da lista
valores.append("cebola")
valores.append(29)
print(valores)

print("*"*80)

#3) inserir elementos especificando posição

valores.insert(4,"chuchu")
valores.insert(0,"abobrinha")
print(valores)

print("_"*80)

#4) acessando um valor em uma posição especifica

print("Elemento na SÉTIMA POSIÇÃO: ", valores[6])
print("Elemento na TERCEIRA POSIÇÃO: ", valores[2])
print("Elemento na PRIMEIRA POSIÇÃO: ",valores[0])
print("Elemento na ÚLTIMA POSIÇÃO: ",valores[-1])
print("Elemento na PENÚLTIMA POSIÇÃO: ",valores[-2])

print("-"*80)

#5) substituindo valores existentes

print("Antes: ",valores)

#substituindo o valor da posição 10
valores[9] = "cenoura"
#Substituindo o valor da posição 0
valores[0] = "beterraba"
#substituindo  valor da ultima posição
valores[-1] = "alho"

print("Depois: ",valores)

print("#"*80)