import math
"""Função para calcular o Índice de massa corporal
de uma pessoa, dados o seu peso em Kg e altura em metrosT """
def imc(peso, altura):
    #peso dividido pela altura ao quadrado
    return peso / (altura ** 2)
resultado = imc(71,1.80)
print("O Imc calculado é", resultado)

def calcular_area(base,altura,tipo):
    if tipo =="R":
        return base*altura
    elif tipo == "T":
        return base*altura/2
    elif tipo == "E":
        return base/2*altura/2* math.pi
    else:
        return None

print("Area retangulo 10x25: ",calcular_area(10,25,"R"))
print("Area triangulo 12x7: ",calcular_area(12,7,"T"))
print("Area elipse 10x10: ",calcular_area(10,10,"E"))