from random import *
#Crear Lista Inicial
palitos = ['-','--','---','----']

#Crear una funcion que se encarguen para mezclar
def mezclar(lista):
    shuffle(lista)
    return lista

#Pedir al usuario que eliga uno de los 4 numeros
def probar_suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)


#Una funcion para Comprobar Intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else:
        print("Te has salvado")
    print(f"Te ha tocado {lista[intento - 1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

###EXAMEN###

def lanzar_dados():
    return randint(1,6),randint(1,6)

def evaluar_jugada(dado1,dado2):
    suma_de_dados = dado1 + dado2
    if suma_de_dados <= 6:
        return f"La suma de tus dados es {suma_de_dados}. Lamentable"
    elif suma_de_dados > 6 and suma_de_dados < 10:
        return f"La suma de tus dados es {suma_de_dados}. Tienes buenas Chances"
    else:
        return f"La suma de tus dados es {suma_de_dados}. parece una jugada ganadora"
    
dado1, dado2 = lanzar_dados()
resultado = evaluar_jugada(dado1,dado2)
print(resultado)



lista_numeros = [1,2,15,7,2,8]
 
def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista
 
def promedio(lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio


lista_numeros = [1,2,15,7,2]

def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop()
    return lista
        
def promedio(lista):
    valor_promedio = sum(lista)/len(lista)
    return valor_promedio

eliminando_duplicados = reducir_lista(lista_numeros)
resultado_promedio = promedio(eliminando_duplicados)
print(eliminando_duplicados)
print(resultado_promedio)



lista_numeros = [1,2,15,7,2,8]
 
import random
 
def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado
 
def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista
    
    
from random import * 
lista_numeros = [1,2,3,4,5,6,7,8,9,10]

def lanzar_moneda():
    resultado = choice(['Cara','Cruz'])
    return resultado
def probar_suerte(moneda,lista):
    if moneda == 'Cara':
        print('La lista se autodestruirá')
        return []
    else:
        print('La lista fue salvada')
        return lista
    
moneda_lanzada = lanzar_moneda()
probando_suerte = probar_suerte(moneda_lanzada,lista_numeros)
print(probando_suerte)



def lanzar_moneda():
    resultado = choice(['Cara','Sello'])
    return resultado

def verificar_moneda(moneda):
    if moneda == 'Cara':
        print('Salio Cara')
    else:
        print('Salio Sello')

resultado_de_lanzar = lanzar_moneda()
resultado_final = verificar_moneda(resultado_de_lanzar)