'''
    RECURSIVIDADE 
    
    Trata-se de uma técnica de programação pela qual
    uma função chama a si mesma, em uma condição diferente
    da inicial. O principal objetivo do uso da recursividade
    é diminuir a complexidade de algoritmos.
'''

def fatorial_iter(num):
    #Verifica se o número é maior que 0
    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível")
    #inicializa o resultado como 1
    res = 1
    #executa o fatorial
    for x in range(num,0,-1): res *= x
    return res  
def fatorial_rec(num):

    if num < 0:
        raise Exception("ERRO: número negativo, cálculo impossível")
    #Se o numero for 1 ou menor, não precisa executar o fatorial e retorna 1
    if num <=1: return 1
    #executa o fatorial recursivamente
    else: return num * fatorial_rec(num-1)
print("7! = ", fatorial_rec(7))
print("0! = ", fatorial_rec(0))
print("-6! = ", fatorial_rec(-6))