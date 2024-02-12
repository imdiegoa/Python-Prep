# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def Factorial(numero):
    if(numero == 1): 
        return 1
    if(numero <= 0):
        return None
    if (numero > 1):
        numero = numero * Factorial(numero - 1)
    return numero

def EsPrimo(numero):
    primo = True
    if type(numero) != int:
        return None
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    return primo
    
class ClaseAnimal:
    def __init__(self, especie, color):
        self.edad = 0
        self.especie = especie
        self.color = color

    def CumplirAnios(self):
        self.edad = self.edad + 1
        return self.edad
