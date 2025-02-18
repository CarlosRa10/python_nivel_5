#Funciones con el uso de return
def multiplicar(num1,num2):
    return num1 * num2

resultado = multiplicar(5,10)
print(resultado)

###EXAMEN###

def potencia(num1,num2):
    return num1**num2
resultado = potencia(3,4)
print(resultado)


dolares = 9
def usd_a_eur(dolares):
    return dolares * 0.90
resultado = usd_a_eur(dolares)
print(resultado)


palabra = "Curso de Python"
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra
