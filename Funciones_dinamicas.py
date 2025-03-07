#Funciones dinamicas
def chequear_3_cifras(numero):
        return numero in range(100,1000)
suma = 282 + 548
resultado = chequear_3_cifras(suma)
print(resultado)

def chequear_3_cifras_con_lista(lista):
    lista_3_cifras = []
    for i in lista:
        if i in range(100,1000):
            #return True
            lista_3_cifras.append(i)
        else:
             pass
    return lista_3_cifras
resultado = chequear_3_cifras_con_lista([555,10,200])
print(resultado)

###EXAMEN###

lista_numeros = [1,-50,502,-5000,755,600,33,61]
 
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True



lista_numeros = [1,50,500,5000,750,600]
 
def suma_menores(lista_numeros):
    suma=0
    for numero in lista_numeros:
        if numero in range(1,1000):
            suma += numero
        else:
            pass
    return suma


lista_numeros = [1,50,502,5000,755,600,33,61]
 
def cantidad_pares(lista_numeros):
    cantidad=0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
        else:
            pass
    return cantidad

lista_numeros = [456,41,9,88,44,2,55,6]
def cantidad_pares(lista_numeros):
    pares = 0
    for i in lista_numeros:
        if i % 2 == 0:
            pares +=1
        else:
            pass
    return pares

print(cantidad_pares)
