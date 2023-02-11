'''
Função para calcular o IMC

'''

def imc (peso, altura):
    # Peso dividido pela altura elevado ao quadrado
    return peso / altura ** 2

resultado = imc(110, 1.70)

print ("O IMC calculado é:", resultado)

from math import pi

def calcular_area (base, altura, tipo):
    if tipo == "R":     #Retângulo
        return base * altura
    elif tipo == "T":   #Triângulo
        return base * altura / 2
    elif tipo == "E":   #Elipse
        return (base / 2) * (altura / 2) * pi
    else:
        return None