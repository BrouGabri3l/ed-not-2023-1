"""
    Dicionario é uma estrutura de dados fornecidas pela linguagem Python, capaz de armazenar multiplos valores em uma única variável, por meio de pares de chave-valor
"""

#Um dicionário é delimitado por chaves {}
# Diferente das listas, que tem posições numeradas, os dicionários
#possuem posições NOMEADAS. Cada uma das posições nomeadas de um 
#Dicionário é chamada PROPRIEDADE.

pessoa = {
    "nome" : "Orozinho Oliveira Osório",
    "sexo": "M",
    "idade" : 71,
    "peso" : 61,
    "altura":1.66,
    "aposentado" : True
}

#Acessando os valores armazenados no dicionário
print("Nome: ", pessoa["nome"])
print("Idade: ", pessoa["idade"])
print("Aposentado: ",pessoa["aposentado"])

#Calculando o IMC (ìndice de massa corporal) da pessoa
imc = pessoa["peso"] / pessoa["altura"] ** 2

print(f"O IMC de {pessoa['nome']} é {imc}")
##############################################
forma1 = {
    "base": 7.5,
    "altura" : 12,
    "tipo" : "R"
}
forma2 = {
    "base": 6,
    "altura" : 2.5,
    "tipo" : "T"
}
forma3 = {
    "base" : 5,
    "altura" : 3,
    "tipo" : "E"
}
from math import pi

def calcular_area(forma):
    if (forma["tipo"] == "R"):
        return forma["base"] * forma["altura"]
    elif(forma["tipo"] == "T"):
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E" :
        return (forma["base"]/2) * (forma["altura"] / 2)*pi
    else:
        return None