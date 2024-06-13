def suma(**Kwargs):
    total = 0
    for clave,valor in Kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total
print(suma(x = 1 ,y = 2 ,z = 3))


def prueba(num1,num2,*args,**Kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for i in args:
        print(f"arg = {i}")

    for clave,valor in Kwargs.items():
        print(f"{clave} = {valor}")
prueba(1,2,100,200,300,400,500,x='uno',y='dos',z='tres')


###EXAMEN###

def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad

print(cantidad_atributos(a=1,b=2,c=3))

def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista
print(lista_atributos(a='uno',b='dos'))


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
describir_persona('Carlos',color_ojos="azules",color_pelo="rubio")