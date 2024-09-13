import math
# THIS IS THE FIRST PYTHON LAB ON THIS SUBJECT.
#TODO,COMPROBAR QUE TODO FUNCIONA CAMBIARLO TODO A INGLES, DOCUMENTAR UN POCO QUÉ HACE CADA COSA

#EXERCISE 1: valor absoluto de un número negativo
def valorAbsoluto(num):
    return abs(num)

print(valorAbsoluto(-5))
print(valorAbsoluto(0))
print(valorAbsoluto(-11))

print("-----------------------------------------------------------------------------")

#EJERCICIO 2:
def sumar(num1, num2):
    return num1 + num2

print(sumar(-5, 2))
print(sumar(5, 2))
print(sumar(0, -12))

print("-----------------------------------------------------------------------------")

#EJERCICIO 3:
def deCentigradosAFahrenheit(temperatura):
    return (9/5)*temperatura + 32

print(deCentigradosAFahrenheit(5))
print(deCentigradosAFahrenheit(-12))
print(deCentigradosAFahrenheit(43))

print("-----------------------------------------------------------------------------")

#EJERCICIO 4:
def calcularRadioEsfera(radio):
    pi = math.pi
    return 4*pi*radio

print(calcularRadioEsfera(4))
print(calcularRadioEsfera(0))
print(calcularRadioEsfera(21.1))

print("-----------------------------------------------------------------------------")

#EJERCICIO 5: NOTA: ESTE EJERCICIO ESTÁ COMENTADO PORQUE LAS EXCEPCIONES DE LOS ASSERT BLOQUEAN EL RESTO DEL SCRIPT.
#DESCOMENTAR PARA EJECUTAR ESTA PARTE Y COMPROBAR QUE FUNCIONA, Y LUEGO VOLVER A COMENTARLO PARA COMPROBAR EL RESTO DE EJERCICIOS.
'''
def calcularIgualdad(a, b, c):
    assert a == b, f"error"
    assert b < c, f"error"
    assert c > a, f"error"

print(calcularIgualdad(4, 4, 6))
print(calcularIgualdad(2, 5, 6))
print(calcularIgualdad(4, 4, 2))
print(calcularIgualdad(0, 0, 0))
'''

print("-----------------------------------------------------------------------------")

#EJERCICIO 6
def calcularDistanciaEuclidea(x1, y1, x2, y2):
    num1 = (x2 - x1) ** 2
    num2 = (y2 - y1) ** 2
    return math.sqrt(num1 + num2)

print(calcularDistanciaEuclidea(2, 4, 2, 3))
print(calcularDistanciaEuclidea(0, 4, 12, 4.2))
print(calcularDistanciaEuclidea(1.2, 1.2, 1.2, 1.2))

print("-----------------------------------------------------------------------------")

#EJERCICIO 7
def calculoDeEjercicio(x, y):
    num1 = (5 * (x ** 3))
    num2 = math.sqrt((x**2) + (y**2))
    num3 = math.exp(math.log(x))
    return num1 + num2 + num3

print(calculoDeEjercicio(5, 5))
print(calculoDeEjercicio(10, 5))
print(calculoDeEjercicio(12.2, 1))

print("-----------------------------------------------------------------------------")

#EJERCICIO 8
def creacionDeLista():
    lista = [1,2,3,4,5]
    return lista

#Esta colección es conocida como 'lista'. Sí que podemos considerarlo un vector númerico, pero las listas de python
#suelen venir con una serie de funciones integradas que nos permiten modificar la lista de más maneras que en arrays
#numéricos de otros lenguajes de programación.

print(creacionDeLista())

print("-----------------------------------------------------------------------------")

#EJERCICIO 9
def sustitucionDeCuatros(lista):
    for i in range(len(lista)):
        if lista[i] == 4:
            lista[i] = 10

    return lista

listaDeCuatros1 = [4,4,4]
listaDeCuatros2 = [4,1,2,2,2,2,3,4,99,0,1,4]

print(sustitucionDeCuatros(listaDeCuatros1))
print(sustitucionDeCuatros(listaDeCuatros2))

print("-----------------------------------------------------------------------------")

#EJERCICIO 10
def numIteracionesCollatzPorCadaNumero(lista):

    listaResultados = []

    for i in range(len(lista)):
        cont = 0
        num = lista[i]
        terminado = False
        while not terminado:
            if num == 1:
                terminado = True
            else:
                if num % 2 == 0:
                    num = num / 2
                    cont += 1
                else:
                    num = (num * 3) + 1
                    cont += 1

        listaResultados.append(cont)

    return listaResultados

lista1 = [1, 3, 17, 22, 7]
lista2 = [21, 31, 11, 10]
lista3 = [6, 11, 27, 32, 33]

print(numIteracionesCollatzPorCadaNumero(lista1))
print(numIteracionesCollatzPorCadaNumero(lista2))
print(numIteracionesCollatzPorCadaNumero(lista3))

print("-----------------------------------------------------------------------------")

#EJERCICIO 11
def inicializacionMatriz():
    matriz = [[1,2,3], [4,5,1], [1,2,-1], [2,2,2], [0,-3, -4], [0,1,-1]]
    return matriz

print(inicializacionMatriz())

print("-----------------------------------------------------------------------------")

#EJERCICIO 12
def contarAparicionesEnMatriz(matriz, num):
    cont = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == num:
                cont = cont + 1
    return cont

matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
matriz3 = [[-1, 2, 3], [-4, 5, -1], [7, -1, 9]]

print(contarAparicionesEnMatriz(matriz1, 5))
print(contarAparicionesEnMatriz(matriz2, 1))
print(contarAparicionesEnMatriz(matriz3, -1))

print("-----------------------------------------------------------------------------")

#EJERCICIO 13
def hayNumeroEntreCuatroYSiete(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (matriz[i][j] > 4 and matriz[i][j] < 7):
                print("Se ha encontrado un número entre el 4 y el 7")
                return True

    print("No se ha encontrado ningun número entre el 4 y el 7")
    return False

matrizA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrizB = [[10, 2, 3], [-1, 0, 1], [8, 9, 7]]
matrizC = [[5, 4, 2], [3, 7, 6], [1, 10, 8]]

print(hayNumeroEntreCuatroYSiete(matrizA))
print(hayNumeroEntreCuatroYSiete(matrizB))
print(hayNumeroEntreCuatroYSiete(matrizC))

print("-----------------------------------------------------------------------------")

#EJERCICIO 14
def compararBooleanosANumeros(listaNumeros, listaBooleanos):
    listaCoincidencias = [0, 0]
    for i in range(len(listaNumeros)):
        if listaNumeros[i] > 0 and listaBooleanos[i] == True:
            listaCoincidencias[0] += 1

        elif listaNumeros[i] <= 0 and listaBooleanos[i] == False:
            listaCoincidencias[1] += 1

    return listaCoincidencias

listaNums1 = [-2, 3, 4, -7, 10, -234]
listaBools1 = [True, True, True, True, False, False]
listaNums2 = [1, -2, 3, 0, -5]
listaBools2 = [True, False, True, False, False]

print(compararBooleanosANumeros(listaNums1, listaBools1))
print(compararBooleanosANumeros(listaNums2, listaBools2))


