class Modulo7:
    def __init__(self, lista1):
        self.lista = lista1

    def verifica_primo(self):
        for i in self.lista:
            if (self.funcion_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.temp(i, origen, destino),'grados',destino)
    
    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))
        
    def funcion_primo(self, x):
        primo = True
        for i in range (2,x):
            if x % i == 0:
                primo = False
                break
        return primo
        
    def valor_modal(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
    
    def temp(self,valor,origen,destino):
        valor_destino = None
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino
    
    def __factorial(self,x):
        resultado = x
        if x % 1 == 0:
            if x > 0:
                while (x > 2):
                    x = x - 1
                    resultado = resultado * x
                print("El factorial es " + str(resultado))
            else:
                print("El numero no es mayor a cero")
        else:
            print("El numero no es entero")
