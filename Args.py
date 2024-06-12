def suma(*args): #el args es una convencion, lo importante es el asterisco
    total = 0
    for i in args:
        total += i
    return total

resultado = suma(10,10,80)
print(resultado)

def suma_facil(*args):
    return sum(args)
print(suma_facil(5,8,50,45))

###EXAMEN###

def suma_cuadrados(*args):
    suma = 0
    for i in args:
        suma += i ** 2
    return suma
print(suma_cuadrados(1,2,3))



def suma_absolutos(*args):
    suma = 0
    for i in args:
        suma += abs(i)
    return suma
print(suma_absolutos(-100))




def numeros_persona(nombre,*args):
    suma_numeros = 0
    for i in args:
        suma_numeros += i
    return print(f"{nombre}, la suma de tus números es {suma_numeros}")
resultado = numeros_persona('Carlos',18,11,25,14)


def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'