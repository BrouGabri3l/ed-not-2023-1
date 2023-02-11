
"""Função para calcular o Índice de massa corporal
de uma pessoa, dados o seu peso em Kg e altura em metrosT """
def imc(peso, altura):
    #peso dividido pela altura ao quadrado
    return peso / (altura ** 2)
resultado = imc(71,1.80)
print("O Imc calculado é", imc)

def calcular_Area(base,altura,tipo):
    if tipo =="Retângulo":
        return base*altura
    elif tipo == "Triângulo":
        return base*altura/2
    elif tipo == "Elipse":
        return base/2*altura/2*math.PI
    else:
        return None