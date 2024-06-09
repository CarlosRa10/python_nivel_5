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
